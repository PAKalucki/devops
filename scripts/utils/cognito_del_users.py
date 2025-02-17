import boto3
import os

client = boto3.client('cognito-idp')

USER_POOL_ID = os.getenv('USER_POOL_ID')

def list_users(client, user_pool_id):
    """List all users in the User Pool"""
    response = client.list_users(UserPoolId=user_pool_id)
    users = response['Users']
    
    while 'PaginationToken' in response:
        response = client.list_users(UserPoolId=user_pool_id, PaginationToken=response['PaginationToken'])
        users.extend(response['Users'])
        
    return users

def delete_users(client, user_pool_id, users):
    """Delete each user from the User Pool"""
    for user in users:
        username = user['Username']
        print(f"Deleting user: {username}")
        client.admin_delete_user(UserPoolId=user_pool_id, Username=username)

def main():
    users = list_users(client, USER_POOL_ID)
    
    if users:
        delete_users(client, USER_POOL_ID, users)
        print("All users deleted successfully.")
    else:
        print("No users found in the User Pool.")

if __name__ == "__main__":
    main()
