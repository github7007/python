import boto3

client = boto3.resource('ec2')

# Filter, find stopped instances
filters = [
      {
        'Name': 'instance-state-name',
        'Values':['running']
      }
]
# Returns all ec2 instances
instances = client.instances.filter(Filters=filters)

for instance in instances:
    instance.stop()
