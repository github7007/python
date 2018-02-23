import boto3
ec2 = boto3.resource('ec2')
sns = boto3.client('sns')
def lambda_handler(event, context):
    # Filter instances based on tag, Key=Env and Value=Dev
    filter = [
          {
              "Name":'tag:Env',
              "Values":['Dev','dev','DEV']
          }
        ]
        # Retreive all dev ec2 instances
    dev_instances = ec2.instances.filter(Filters=filter)
    instance_ids = []
    for dev_instance in dev_instances:
        instance_ids.append(dev_instance.id)
        dev_instance.start()

    # send email notification
    sns.publish(TopicArn='arn:aws:sns:us-west-2:915530126681:lambda',
                Subject='Dev Servers started',
                Message=str(instance_ids))
    return 'Success'
