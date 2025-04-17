#!/usr/bin/env bash

OUTFILE="disabledAssignments.csv"
echo "subscriptionId,scope,roleDefinitionName,principalId,principalName" > "$OUTFILE"

disabled_ids=$(az ad user list \
               --filter "accountEnabled eq false" \
               --query "[].id" -o tsv)

for sub in $(az account list --query "[].id" -o tsv); do
  az account set --subscription "$sub"
  for id in $disabled_ids; do
    az role assignment list --assignee "$id" --all --include-inherited \
      --query "[].{subscriptionId:'$sub',scope:scope,roleDefinitionName:roleDefinitionName,principalId:principalId,principalName:principalName}" -o json |
      jq -r '.[] | [.subscriptionId,.scope,.roleDefinitionName,.principalId,.principalName] | @csv' \
      >> "$OUTFILE"
  done
done
