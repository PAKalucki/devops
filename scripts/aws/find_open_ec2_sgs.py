import boto3

# Create EC2 resource
ec2 = boto3.resource('ec2')

def check_rule(rule, port):
    for ip_range in rule['IpRanges']:
        if ip_range['CidrIp'] == '0.0.0.0/0' and rule['FromPort'] == port:
            return True
    for ipv6_range in rule['Ipv6Ranges']:
        if ipv6_range['CidrIpv6'] == '::/0' and rule['FromPort'] == port:
            return True
    return False

def check_security_group(sg):
    for rule in sg.ip_permissions:
        # Ignore ICMP
        if rule.get('IpProtocol') in ['icmp', 'icmpv6', '1', '58']:
            continue
        if 'FromPort' in rule and 'ToPort' in rule:
            for port in range(rule['FromPort'], rule['ToPort']+1):
                if port not in [80, 443] and (check_rule(rule, port)):
                    return True
    return False

# Create a map from security group to instances
sg_to_instances = {}
for instance in ec2.instances.all():
    for sg in instance.security_groups:
        if sg['GroupId'] not in sg_to_instances:
            sg_to_instances[sg['GroupId']] = []
        sg_to_instances[sg['GroupId']].append(instance.id)

# Loop through all the security groups
for security_group in ec2.security_groups.all():
    if check_security_group(security_group) and security_group.id in sg_to_instances:
        print(f"Security Group {security_group.id} allows traffic from any source on ports other than 80 and 443.")
        print(f"The following instances are associated with this security group:")
        for instance_id in sg_to_instances[security_group.id]:
            print(f"  Instance ID: {instance_id}")
