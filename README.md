# Start-Stop AWS EC2 Instances

This is a simple Python script that allows you to start or stop AWS EC2 instances using the Boto3 library.

## Prerequisites

- Python 3.x
- Boto3 library
- AWS access key and secret access key with appropriate permissions

## Installation

1. Clone the repository or download the source code.

2. Create a virtual environment (optional but recommended):

3. Install the required dependencies:


## Configuration

1. Open the `main.py` file and update the following variables with your AWS credentials and desired region:

AWS_SERVER_PUBLIC_KEY = "<YOUR_AWS_SERVER_PUBLIC_KEY>"  # Replace with your AWS access key

AWS_SERVER_SECRET_KEY = "<YOUR_AWS_SERVER_SECRET_KEY>"  # Replace with your AWS secret access key

region = "<YOUR_DESIRED_AWS_REGION>"  # Replace with your desired AWS region

## Usage
$ python main.py START  # Start the instances

$ python main.py STOP   # Stop the instances