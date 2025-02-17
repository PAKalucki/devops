import boto3

# Initialize a boto3 client for Lambda
lambda_client = boto3.client('lambda')

def delete_old_lambda_layer_versions(layer_name, keep_last_n=10):
    """
    Deletes all but the last N versions of a specified AWS Lambda Layer.

    Parameters:
    - layer_name: The name of the Lambda Layer to clean up.
    - keep_last_n: The number of most recent versions to keep. Defaults to 10.
    """

    # List all versions of the specified Lambda Layer
    response = lambda_client.list_layer_versions(LayerName=layer_name)
    versions = response['LayerVersions']

    # Sort versions by version number in ascending order
    versions.sort(key=lambda x: x['Version'])

    # Calculate the number of versions to delete
    versions_to_delete = len(versions) - keep_last_n

    # Delete old versions if there are more than keep_last_n versions
    if versions_to_delete > 0:
        for version in versions[:versions_to_delete]:
            version_number = version['Version']
            print(f"Deleting version {version_number} of layer {layer_name}...")
            lambda_client.delete_layer_version(LayerName=layer_name, VersionNumber=version_number)
            print(f"Version {version_number} deleted.")
    else:
        print("No versions to delete. Keeping the last 10 versions.")

# Example usage
layer_name = "layer"
for x in range(0, 100):
    delete_old_lambda_layer_versions(layer_name)
