import boto3


# To create ec2 intance
def create_instance():

    # security_group_id_input = input("Enter the security group id: ")

    name_of_the_instances = input("Enter the Instances Name: ")

    # security_group_ids.append(security_group_id_input)

    security_group_ids = ['sg-0673eea67ae7c452c']

    ec2 = boto3.resource('ec2')

    security_group_ids = []

    instance = ec2.create_instances(
        ImageId='ami-053b0d53c279acc90',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName="windows_key",
        SecurityGroupIds=security_group_ids
    )

     # Wait for the instance to be in a running state
    instance[0].wait_until_running()

    # Add a "Name" tag to the instance
    instance[0].create_tags(Tags=[{'Key': 'Name', 'Value': name_of_the_instances}])

    return instance[0]  # Return the first (and only) instance in the list


# To list all the instances
def instance_details():

    ec2 = boto3.client('ec2')

    response = ec2.describe_instances(
        
    ).get("Reservations")
    ids = []
    for reser in response:
        for insta in reser['Instances']:
            ids.append(insta["InstanceId"])

    return ids


# To stop and terminate the ec2 intances
def stop_and_terminate():

    ec2 = boto3.resource('ec2')

    # Calling instance_details function to get the running instances ids.
    # instances = instance_details()
    instance_id = input("Enter the instance id: ")

    # print(instance_id)

    stop = ec2.instances.filter(InstanceIds=[instance_id]).stop()
    print(f"{instance_id} Stopped")

    # To terminate Instance
    terminate = ec2.instances.filter(InstanceIds=[instance_id]).terminate()
    print(f"{terminate} Terminatted")


# print(instance_details())
stop_and_terminate()

# instances = create_instance()
# print(instances.id)