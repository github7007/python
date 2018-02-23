# Launch EC2 instance using python(boto3)
import boto3
ec2 = boto3.client('ec2')
ec2.run_instances(ImageId='ami-bf4193c7',
                  InstanceType='t2.micro',
                  MinCount=1,
                  MaxCount=1)
