import argparse
import logging
import os
from pathlib import Path

import requests
from azure.communication.email import EmailClient
from azure.identity import AzureCliCredential, DefaultAzureCredential

GRAPH_URL = "https://graph.microsoft.com/v1.0"
GRAPH_SCOPE = "https://graph.microsoft.com/.default"


def _graph_headers(credential: AzureCliCredential) -> dict:
    token = credential.get_token(GRAPH_SCOPE).token
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def add_user_to_group(user_email: str, group_name: str) -> None:
    """Add a user to an Entra ID group using Microsoft Graph."""
    credential = AzureCliCredential()
    headers = _graph_headers(credential)

    logging.info("Adding %s to group %s", user_email, group_name)

    user_resp = requests.get(f"{GRAPH_URL}/users/{user_email}", headers=headers)
    if user_resp.status_code != 200:
        logging.error("Failed to resolve user: %s", user_resp.text)
        user_resp.raise_for_status()
    user_id = user_resp.json()["id"]

    group_resp = requests.get(
        f"{GRAPH_URL}/groups",
        headers=headers,
        params={"$filter": f"displayName eq '{group_name}'"},
    )
    if group_resp.status_code != 200:
        logging.error("Failed to resolve group: %s", group_resp.text)
        group_resp.raise_for_status()
    groups = group_resp.json().get("value", [])
    if not groups:
        raise RuntimeError(f"Group {group_name} not found")
    group_id = groups[0]["id"]

    add_resp = requests.post(
        f"{GRAPH_URL}/groups/{group_id}/members/$ref",
        headers=headers,
        json={"@odata.id": f"{GRAPH_URL}/directoryObjects/{user_id}"},
    )
    if add_resp.status_code not in (200, 204):
        logging.error("Failed to add user to group: %s", add_resp.text)
        add_resp.raise_for_status()
    logging.info("User added to group successfully")


def _load_email_template() -> str:
    template_path = Path(__file__).with_name("email_template.txt")
    with template_path.open("r", encoding="utf-8") as handle:
        return handle.read()


def send_email(user_email: str) -> None:
    """Send a notification email via Azure Communication Services."""
    endpoint = os.getenv("ACS_ENDPOINT")
    sender = os.getenv("ACS_SENDER_ADDRESS")
    if not endpoint or not sender:
        raise RuntimeError("ACS_ENDPOINT and ACS_SENDER_ADDRESS must be set")

    credential = DefaultAzureCredential()
    client = EmailClient(endpoint, credential)

    content = _load_email_template()
    message = {
        "senderAddress": sender,
        "recipients": {"to": [{"address": user_email}]},
        "content": {
            "subject": "Access granted",
            "plainText": content,
        },
    }

    logging.info("Sending email to %s", user_email)
    try:
        poller = client.begin_send(message)
        result = poller.result()
        logging.info("Email sent with message ID %s", result["messageId"])
    except Exception as exc:  # pylint: disable=broad-except
        logging.error("Failed to send email: %s", exc)
        raise


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add user to EntraID group and send onboarding email",
    )
    parser.add_argument("user_email", nargs="?", help="Email of the user to onboard")
    parser.add_argument("group_name", nargs="?", help="Target EntraID group")
    parser.add_argument(
        "--file",
        "-f",
        dest="file",
        help="File with 'user_email group_name' per line",
    )

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    def process(email: str, group: str) -> None:
        add_user_to_group(email, group)
        send_email(email)

    try:
        if args.file:
            with open(args.file, "r", encoding="utf-8") as handle:
                for line in handle:
                    parts = line.strip().split()
                    if len(parts) != 2:
                        logging.warning("Skipping malformed line: %s", line.strip())
                        continue
                    process(parts[0], parts[1])
        else:
            if not args.user_email or not args.group_name:
                parser.error("user_email and group_name required unless --file is used")
            process(args.user_email, args.group_name)
    except Exception as exc:  # pylint: disable=broad-except
        logging.error("Onboarding failed: %s", exc)


if __name__ == "__main__":
    main()
