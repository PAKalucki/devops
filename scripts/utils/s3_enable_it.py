import boto3

def enable_intelligent_tiering_and_lifecycle():
    s3_client = boto3.client('s3')

    # List all S3 buckets
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Iterate over each bucket and enable intelligent tiering and lifecycle rule
    for bucket_name in buckets:
        try:
            # Check for existing lifecycle rules
            try:
                lifecycle = s3_client.get_bucket_lifecycle_configuration(Bucket=bucket_name)
                if lifecycle['Rules']:
                    print(f"Bucket {bucket_name} already has lifecycle rules. Skipping.")
                    continue
            except s3_client.exceptions.ClientError as e:
                if e.response['Error']['Code'] != 'NoSuchLifecycleConfiguration':
                    print(f"Error checking lifecycle configuration for bucket {bucket_name}: {e}")
                    continue

            # Add lifecycle rule for Intelligent Tiering
            s3_client.put_bucket_lifecycle_configuration(
                Bucket=bucket_name,
                LifecycleConfiguration={
                    'Rules': [
                        {
                            'ID': 'MoveToIntelligentTieringImmediately',
                            'Status': 'Enabled',
                            'Filter': {'Prefix': ''},  # Apply to all objects
                            'Transitions': [
                                {
                                    'Days': 0,
                                    'StorageClass': 'INTELLIGENT_TIERING'
                                }
                            ]
                        }
                    ]
                }
            )
            print(f"Lifecycle rule added to bucket: {bucket_name}")

            # Configure and enable intelligent tiering
            s3_client.put_bucket_intelligent_tiering_configuration(
                Bucket=bucket_name,
                Id='IntelligentTieringConfiguration',
                IntelligentTieringConfiguration={
                    'Id': 'IntelligentTieringConfiguration',
                    'Status': 'Enabled',
                    'Tierings': [
                        {
                            'Days': 730,
                            'AccessTier': 'ARCHIVE_ACCESS'
                        }
                    ]
                }
            )
            print(f"Intelligent Tiering enabled for bucket: {bucket_name}")

        except s3_client.exceptions.ClientError as e:
            print(f"Error processing bucket {bucket_name}: {e}")

if __name__ == "__main__":
    enable_intelligent_tiering_and_lifecycle()
