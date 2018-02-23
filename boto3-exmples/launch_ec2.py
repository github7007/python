# Launch ec2 instance with python boto3
import boto3

client = boto3.client('ec2')
client.run_instances(
        ImageId = 'ami-32cf7b4a',
        InstanceType = 't2.micro',
        MinCount=1,
        MaxCount=1
)
