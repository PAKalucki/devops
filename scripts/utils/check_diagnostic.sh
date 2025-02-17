#!/bin/bash

# Get a list of all subscriptions
subscriptions=$(az account list --query "[].id" -o tsv)

# Loop through each subscription
for sub in $subscriptions; do
  echo "Checking subscription: $sub"

  # Set the current subscription
  az account set --subscription $sub

  # Get a list of all resource groups in the current subscription
  resourceGroups=$(az group list --query "[].name" -o tsv)

  # Loop through each resource group
  for rg in $resourceGroups; do
    # echo "Checking resources in resource group: $rg"
    
    # Get all resources in the resource group
    resources=$(az resource list --resource-group $rg --query "[].id" -o tsv)
    
    # Loop through each resource
    for resource in $resources; do
      # echo "Checking resource: $resource"
      
      # Get diagnostic settings for the resource
      diagnosticSettings=$(az monitor diagnostic-settings list --resource $resource --query "[].storageAccountId" -o tsv)
      
      # Check if diagnostic settings are configured to send logs to a storage account
      if [ -z "$diagnosticSettings" ]; then
        echo ""
        # echo "No diagnostic settings sending logs to a storage account for resource: $resource"
      else
        # Get the storage account name from the storage account ID
        storageAccountName=$(az storage account show --ids $diagnosticSettings --query "name" -o tsv)
        echo "Diagnostic settings sending logs to storage account: $storageAccountName for resource: $resource"
      fi
    done
  done
done
