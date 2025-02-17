#!/bin/bash

# Variables - source and destination NSGs
SOURCE_NSG=""
DEST_NSG=""
RESOURCE_GROUP=""

check_and_copy_rules() {
    local direction=$1

    # Get the list of all rules from the source NSG
    all_rules=$(az network nsg rule list --nsg-name $SOURCE_NSG --resource-group $RESOURCE_GROUP --query '[].{Name:name, Direction:direction}' -o tsv)

    # Filter rules by direction
    source_rules=$(echo "$all_rules" | grep -i "$direction" | awk '{print $1}')

    # Get the list of rules from the destination NSG
    dest_rules=$(az network nsg rule list --nsg-name $DEST_NSG --resource-group $RESOURCE_GROUP --query '[].{Name:name}' -o tsv)

    for rule in $source_rules; do
        # Check if the rule exists in the destination NSG
        if ! echo "$dest_rules" | grep -q "$rule"; then
            echo "Rule $rule does not exist in $DEST_NSG. Copying..."
            
            # Get the rule details from the source NSG
            rule_details=$(az network nsg rule show --nsg-name $SOURCE_NSG --resource-group $RESOURCE_GROUP --name $rule --query "{name:name,priority:priority,access:access,direction:direction,protocol:protocol,sourcePortRange:sourcePortRange,destinationPortRange:destinationPortRange,sourceAddressPrefix:sourceAddressPrefix,destinationAddressPrefix:destinationAddressPrefix}" -o json)
            echo $rule_details
            # Extract the protocol and ensure it's valid
            protocol=$(echo $rule_details | jq -r '.protocol')
            name=$(echo $rule_details | jq -r '.name')
            priority=$(echo $rule_details | jq -r '.priority')
            access=$(echo $rule_details | jq -r '.access')
            direction=$(echo $rule_details | jq -r '.direction')
            sourcePortRange=$(echo $rule_details | jq -r '.sourcePortRange')
            destinationPortRange=$(echo $rule_details | jq -r '.destinationPortRange')
            sourceAddressPrefix=$(echo $rule_details | jq -r '.sourceAddressPrefix')
            destinationAddressPrefix=$(echo $rule_details | jq -r '.destinationAddressPrefix')

            # Create the rule in the destination NSG with the same properties
            az network nsg rule create --nsg-name $DEST_NSG --resource-group $RESOURCE_GROUP --name "$name"\
                --priority "$priority" --access "$access" \
                --direction "$direction" --protocol "$protocol" \
                --source-port-ranges "$sourcePortRange" \
                --destination-port-ranges "$destinationPortRange" \
                --source-address-prefixes "$sourceAddressPrefix" \
                --destination-address-prefixes "$destinationAddressPrefix"
                
            echo "Rule $rule copied to $DEST_NSG."
        else
            echo "Rule $rule already exists in $DEST_NSG. Skipping..."
        fi
    done
}

# Check inbound rules
echo "Checking inbound rules..."
check_and_copy_rules "Inbound"

# Check outbound rules
echo "Checking outbound rules..."
check_and_copy_rules "Outbound"

echo "Process completed."