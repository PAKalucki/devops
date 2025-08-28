# Azure Onboarding Script

This script adds a user to an Entra ID group and sends a notification email via Azure Communication Services.

## Prerequisites
- Run `az login` to authenticate with Azure CLI.
- Set environment variables:
  - `ACS_ENDPOINT` – Azure Communication Services endpoint
  - `ACS_SENDER_ADDRESS` – Verified sender email address
- Ensure `email_template.txt` contains the email body.

## Usage
```
python azure_onboard.py <user_email> <group_name> <avd_name>
```
`avd_name` will be inserted into the email template to inform the user of their granted access.
