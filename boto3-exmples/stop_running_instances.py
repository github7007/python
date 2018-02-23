import boto3

ec2 = boto3.resource('ec2')

filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['stopped123']
        },
        {
            'Name': 'tag:Env',
            'Values': ['Dev']
        }
    ]
instances = ec2.instances.filter(Filters=filters)

for instance in instances:
    print(instance)
