# Stop EC2 instance using python(boto3)
import boto3
ec2 = boto3.client('ec2')
ec2.stop_instances(InstanceIds=['i-07a39f917a5506b9e'])
