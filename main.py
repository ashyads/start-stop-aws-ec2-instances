import sys
import boto3

# AWS credentials
AWS_SERVER_PUBLIC_KEY = ""  # Replace with your AWS access key
AWS_SERVER_SECRET_KEY = ""  # Replace with your AWS secret access key

# Create a session using the AWS credentials
session = boto3.Session(
    aws_access_key_id=AWS_SERVER_PUBLIC_KEY,
    aws_secret_access_key=AWS_SERVER_SECRET_KEY,
)

region = 'ap-south-1'  # Replace with your desired AWS region

# Create an EC2 client using the session and region
client = session.client('ec2', region_name=region)

# List of instance IDs that you want to start or stop
ON_OFF_INSTANCES = ['i-0a97kfs90364d29']

# Get the action from the command line arguments (first argument)
action = sys.argv[1]

# Loop through each instance and perform the specified action
for instance in ON_OFF_INSTANCES:
    if action == "START":
        # Check if the instance is not already running
        response = client.describe_instances(InstanceIds=[instance])
        if response['Reservations'][0]['Instances'][0]['State']['Name'] != 'running':
            # Start the instance if it's not running
            client.start_instances(InstanceIds=[instance])
            print(f"Started instance {instance}")
        else:
            print(f"Instance {instance} is already running.")
    elif action == "STOP":
        # Check if the instance is not already stopped
        response = client.describe_instances(InstanceIds=[instance])
        if response['Reservations'][0]['Instances'][0]['State']['Name'] != 'stopped':
            # Stop the instance if it's not stopped
            client.stop_instances(InstanceIds=[instance])
            print(f"Stopped instance {instance}")
        else:
            print(f"Instance {instance} is already stopped.")
    else:
        print("Invalid action. Please specify either 'START' or 'STOP' in the command line.")
