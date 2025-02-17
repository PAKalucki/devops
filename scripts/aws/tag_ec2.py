import boto3

# Instantiate the EC2 resource object
ec2 = boto3.resource('ec2')

# Function to add tag to an instance
def add_tag_to_instance(instance_id, tag_key, tag_value):
    try:
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[
                {
                    'Key': tag_key,
                    'Value': tag_value
                },
            ]
        )
        print(f"Successfully added tag to instance: {instance_id}")
    except Exception as e:
        print(f"Failed to add tag to instance: {instance_id}. Reason: {e}")

# Read file and get instance IDs
with open('instances.txt', 'r') as file:
    instance_ids = file.read().splitlines()

# Add tag to each instance
tag_key = 'VantaUserDataStored'
tag_value = 'true'

for instance_id in instance_ids:
    add_tag_to_instance(instance_id, tag_key, tag_value)
