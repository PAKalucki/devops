#!/bin/bash
aws s3api list-buckets --query "Buckets[].Name" | jq -r .[] | while read line; do 
   echo "Checking bucket: $line"; 
   aws s3api get-bucket-acl --bucket $line | jq '.Grants[] | select(.Grantee.URI)'; 
done
