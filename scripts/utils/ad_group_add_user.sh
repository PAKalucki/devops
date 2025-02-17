#!/bin/bash

USER=$1
TEAM=${2:-DosimetryWorldTeam}
echo "Adding user ${USER} to ${TEAM}"
USER_SHOW=$(az ad user show --id "$1")
echo "${USER_SHOW}"

USER_ID=$(echo "${USER_SHOW}" | jq -r .id )
echo "USER ID: ${USER_ID}"

az ad group member add --group "${TEAM}" --member-id "${USER_ID}"

echo "Current members:"
az ad group member list --group "${TEAM}" | jq '.[].mail'