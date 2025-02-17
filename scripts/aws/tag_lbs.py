import boto3

def add_tags_to_load_balancers():
    client = boto3.client('elbv2')
    response = client.describe_load_balancers()

    for load_balancer in response['LoadBalancers']:
        arn = load_balancer['LoadBalancerArn']
        client.add_tags(
            ResourceArns=[arn],
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'XXX'
                },
            ]
        )

if __name__ == '__main__':
    add_tags_to_load_balancers()
