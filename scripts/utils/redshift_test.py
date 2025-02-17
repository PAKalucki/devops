import boto3
from datetime import datetime

# Configuration
cluster_identifier = 'dev-cluster'
database = 'submarine'
region_name = 'us-east-1'
sql_query = 'SELECT id, child_id, user_id, organization_id, school_id, classroom_id, start_date, end_date, game_duration FROM ign_sessions where organization_id = 1300 and game_duration >= 150;'  # Example test query

# Create a Redshift Data API client with IAM role-based authentication
data_client = boto3.client('redshift-data', region_name=region_name)

def run_query():
    start_time = datetime.now()
    # Execute the SQL query
    response = data_client.execute_statement(
        ClusterIdentifier=cluster_identifier,
        Database=database,
        DbUser='admin',
        Sql=sql_query
    )
    
    query_id = response['Id']
    print(f"Query submitted, ID: {query_id}")

    # Wait for the query to complete
    status = 'SUBMITTED'
    while status in ['SUBMITTED', 'STARTED', 'PICKED']:
        response = data_client.describe_statement(Id=query_id)
        status = response['Status']
        if status in ['FAILED', 'FINISHED']:
            break
        print(f"Query status: {status}")
    
    if status == 'FINISHED':
        print("Query finished successfully.")
        # Fetch the result
        result_response = data_client.get_statement_result(Id=query_id)
        records = result_response['Records']
        
        # Example of how to print the results, customize as needed
        for record in records:
            print(record)

        end_time = datetime.now()  # End timing
        execution_time = end_time - start_time  # Calculate execution time
        print(f"Execution time: {execution_time}")
    elif status == 'FAILED':
        print(f"Query failed with status: {status}")
        # Correctly retrieve more information about the failure
        print(str(response))
    else:
        print(f"Query ended with status: {status}")

if __name__ == "__main__":
    run_query()