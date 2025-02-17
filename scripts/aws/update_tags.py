import boto3

# Setup session
# if your AWS ACCESS KEY and SECRET are configured, this will automatically use those
session = boto3.Session()

ec2 = session.resource('ec2', region_name='us-west-2')  # change to your region

# Define the tag filter
tag_filter = [{
    'Name': 'tag:Backup',
    'Values': ['Weekly']
}]

# Get all instances that have a tag with key 'Backup' and value 'Weekly'
instances = ec2.instances.filter(Filters=tag_filter)

for instance in instances:
    # For each instance, print its ID
    print(f'Changing tag for instance {instance.id}...')

    # Define new tags
    new_tags = [
        {
            'Key': 'Backup',
            'Value': 'Daily'
        }
    ]

    # Remove the old tag
    instance.create_tags(Tags=[{'Key': 'Backup', 'Value': ''}])

    # Add the new tag
    instance.create_tags(Tags=new_tags)
