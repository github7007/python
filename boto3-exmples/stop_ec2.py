# Stop ec2 instance
import boto3

client = boto3.client('ec2')
client.stop_instances(InstanceIds = ['i-0da555cb80d0cc44c'])
