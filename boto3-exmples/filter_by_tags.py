import boto3

client = boto3.resource('ec2')

# Filter, find stopped instances
filters = [
      {
        'Name': 'tag:Backup',
        'Values':['Yes']
      }
]
# Returns all ec2 instances
instances = client.instances.filter(Filters=filters)

for instance in instances:
    print(instance.instance_id)
