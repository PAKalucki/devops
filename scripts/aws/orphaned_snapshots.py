import boto3

def find_orphaned_snapshots(region_name):
    ec2 = boto3.resource('ec2', region_name=region_name)

    used_snapshots = set()

    # Get snapshots associated with EBS volumes
    volumes = ec2.volumes.all()
    for volume in volumes:
        if volume.snapshot_id:
            used_snapshots.add(volume.snapshot_id)

    # Get snapshots associated with AMIs
    images = ec2.images.filter(Owners=['self'])
    for image in images:
        for device in image.block_device_mappings:
            if 'Ebs' in device and 'SnapshotId' in device['Ebs']:
                used_snapshots.add(device['Ebs']['SnapshotId'])

    all_snapshots = ec2.snapshots.filter(OwnerIds=['self'])
    orphan_snapshots = [s for s in all_snapshots 
                        if s.snapshot_id not in used_snapshots 
                        and not is_managed_by_aws_backup(s)]
    
    return orphan_snapshots

def is_managed_by_aws_backup(snapshot):
    if snapshot.tags is None:
        return False
    for tag in snapshot.tags:
        if tag['Key'] == 'aws:backup:source-resource':
            return True
    return False

def get_name(snapshot):
    if snapshot.tags is None:
        return ''
    for tag in snapshot.tags:
        if tag['Key'] == 'Name':
            return tag['Value']
    return ''

def delete_snapshots(snapshots):
    for snapshot in snapshots:
        snapshot.delete()

if __name__ == "__main__":
    region = 'us-west-2'  # modify to match your AWS region
    orphan_snapshots = find_orphaned_snapshots(region)

    print("Orphaned Snapshots:")
    for snapshot in orphan_snapshots:
        name = get_name(snapshot)
        print(f"Name: {name}, Snapshot ID: {snapshot.snapshot_id}")

    # Uncomment the following line if you wish to delete the orphaned snapshots
    # delete_snapshots(orphan_snapshots)
