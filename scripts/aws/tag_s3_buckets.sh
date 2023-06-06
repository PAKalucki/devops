#!/bin/bash

# Text file containing the bucket names
BUCKET_FILE='buckets.txt'

# AWS CLI command for adding tag to a bucket
TAG_CMD='aws s3api put-bucket-tagging'

# Iterate through each line of the file
while IFS= read -r line
do
  echo "Adding tag to bucket: $line"
  $TAG_CMD --bucket "$line" --tagging 'TagSet=[{Key=TAG,Value=true}]'
done < "$BUCKET_FILE"
