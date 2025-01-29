# import boto3

# AWS configuration
# aws_region = 'us-east-1'  # Change to your preferred AWS region
# ami_id = 'ami-0df8c184d5f6ae949'  # Example AMI ID for Amazon Linux 2, change as needed
# instance_type = 't2.micro'  # Instance type
# key_name = 'RP_30'  # Replace with your key pair name
# security_group_id = 'sg-0038fc47dec03a730'  # Replace with your security group ID

# import boto3
# import time

# def createInstance(number):
#    ec2 = boto3.client('ec2', region_name='us-east-1')
#    conn = ec2.run_instances(ImageId='ami-0df8c184d5f6ae949', 
#                            InstanceType='t2.micro',
#                            MinCount=1, 
#                            MaxCount=number
#                               )

# def list_instances(region_name):
#     ec2_client = boto3.client('ec2', region_name=region_name)
#     instance_ids = []

#     try:
#         response = ec2_client.describe_instances()
#         for reservation in response['Reservations']:
#             for instance in reservation['Instances']:
#                 if instance['State']['Name'] == 'running':  
#                     instance_ids.append(instance['InstanceId'])
#         print(f"Found instances: {instance_ids}")
#     except Exception as e:
#         print(f"An error occurred while listing instances: {e}")

#     return instance_ids

# def create_load_balancer(region_name, instance_ids):
#     """Create a load balancer and register the listed instances."""
#     ec2_client = boto3.client('ec2', region_name=region_name)
#     elb_client = boto3.client('elbv2', region_name=region_name)

#     if not instance_ids:
#         print("No instances to register with the load balancer.")
#         return

#     try:
#         target_group_response = elb_client.create_target_group(
#             Name='my-target-group',
#             Protocol='HTTP',
#             Port=80,
#             VpcId=ec2_client.describe_vpcs()['Vpcs'][0]['VpcId'],
#             TargetType='instance',
#             HealthCheckProtocol='HTTP',
#             HealthCheckPath='/',
#             HealthCheckIntervalSeconds=30,
#             HealthCheckTimeoutSeconds=5,
#             HealthyThresholdCount=5,
#             UnhealthyThresholdCount=2
#         )
#         target_group_arn = target_group_response['TargetGroups'][0]['TargetGroupArn']
#         print(f"Created Target Group: {target_group_arn}")

#         targets = [{'Id': instance_id} for instance_id in instance_ids]
#         elb_client.register_targets(TargetGroupArn=target_group_arn, Targets=targets)
#         print(f"Registered instances: {instance_ids}")

#         load_balancer_response = elb_client.create_load_balancer(
#             Name='my-load-balancer',
#             Subnets=[subnet['SubnetId'] for subnet in ec2_client.describe_subnets()['Subnets']],
#             SecurityGroups=[sg['GroupId'] for sg in ec2_client.describe_security_groups()['SecurityGroups'] if sg['GroupName'] == 'default'],
#             Scheme='internet-facing',
#             Type='application',
#             IpAddressType='ipv4'
#         )
#         load_balancer_arn = load_balancer_response['LoadBalancers'][0]['LoadBalancerArn']
#         print(f"Created Load Balancer: {load_balancer_arn}")

        
#         elb_client.create_listener(
#             LoadBalancerArn=load_balancer_arn,
#             Protocol='HTTP',
#             Port=80,
#             DefaultActions=[{
#                 'Type': 'forward',
#                 'TargetGroupArn': target_group_arn
#             }]
#         )
#         print("Listener created for Load Balancer.")

#         return load_balancer_arn

#     except Exception as e:
#         print(f"An error occurred: {e}")

# def create_launch_template(region_name, instance_id):
#     ec2_client = boto3.client('ec2', region_name=region_name)

#     try:
#         instance = ec2_client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
#         launch_template_response = ec2_client.create_launch_template(
#             LaunchTemplateName=template_name,
#             LaunchTemplateData={
#                 'ImageId': instance['ImageId'],
#                 'InstanceType': instance['InstanceType'],
#                 'SecurityGroupIds': [sg['GroupId'] for sg in instance['SecurityGroups']],
#             }
#         )
#         launch_template_id = launch_template_response['LaunchTemplate']['LaunchTemplateId']
#         print(f"Created Launch Template: {launch_template_id}")
#         return launch_template_id

#     except Exception as e:
#         print(f"An error occurred while creating launch template: {e}")
#         return None

# def create_auto_scaling_group(region_name, launch_template_id):
#     as_client = boto3.client('autoscaling', region_name=region_name)

#     try:
#         # Create Auto Scaling group
#         as_client.create_auto_scaling_group(
#             AutoScalingGroupName='my-auto-scaling-group',
#             LaunchTemplate={
#                 'LaunchTemplateId': launch_template_id,
#                 'Version': '$Latest'
#             },
#             MinSize=1,
#             MaxSize=1,
#             DesiredCapacity=1,
#             VPCZoneIdentifier=','.join(
#                 [subnet['SubnetId'] for subnet in boto3.client('ec2', region_name=region_name).describe_subnets()['Subnets']]
#             )
#         )
#         print("Auto Scaling group created successfully.")

#     except Exception as e:
#         print(f"An error occurred while creating the Auto Scaling group: {e}")

# region = "us-east-1"  
# # no_of_Ins = input('Enter no of Instances to be created :')
# # createInstance(no_of_Ins)
# instances = list_instances(region)

# # Wait for instances to be running before proceeding
# print("Waiting for instances to initialize...")
# time.sleep(120)

# template_name=input('Enter the template name :')
# create_load_balancer(region, instances)
# if instances:
#     launch_template_id = create_launch_template(region, instances[0])

#     if launch_template_id:
#         create_auto_scaling_group(region, launch_template_id)
# else:
#     print("No running instances found to create an Auto Scaling group.")



import boto3
import time

def createInstance(number):
   ec2 = boto3.client('ec2', region_name='us-east-1')
   conn = ec2.run_instances(ImageId='ami-0df8c184d5f6ae949', 
                           InstanceType='t2.micro',
                           MinCount=1, 
                           MaxCount=int(number)
                              )

def list_instances(region_name):
    ec2_client = boto3.client('ec2', region_name=region_name)
    instance_ids = []

    try:
        response = ec2_client.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] == 'running':  
                    instance_ids.append(instance['InstanceId'])
        print(f"Found instances: {instance_ids}")
    except Exception as e:
        print(f"An error occurred while listing instances: {e}")

    return instance_ids

def create_load_balancer(region_name, instance_ids):
    ec2_client = boto3.client('ec2', region_name=region_name)
    elb_client = boto3.client('elbv2', region_name=region_name)

    if not instance_ids:
        print("No instances to register with the load balancer.")
        return

    try:
        target_group_response = elb_client.create_target_group(
            Name='my-target-group',
            Protocol='HTTP',
            Port=80,
            VpcId=ec2_client.describe_vpcs()['Vpcs'][0]['VpcId'],
            TargetType='instance',
            HealthCheckProtocol='HTTP',
            HealthCheckPath='/',
            HealthCheckIntervalSeconds=30,
            HealthCheckTimeoutSeconds=5,
            HealthyThresholdCount=5,
            UnhealthyThresholdCount=2
        )
        target_group_arn = target_group_response['TargetGroups'][0]['TargetGroupArn']
        print(f"Created Target Group: {target_group_arn}")

        targets = [{'Id': instance_id} for instance_id in instance_ids]
        elb_client.register_targets(TargetGroupArn=target_group_arn, Targets=targets)
        print(f"Registered instances: {instance_ids}")

        load_balancer_response = elb_client.create_load_balancer(
            Name='my-load-balancer',
            Subnets=[subnet['SubnetId'] for subnet in ec2_client.describe_subnets()['Subnets']],
            SecurityGroups=[sg['GroupId'] for sg in ec2_client.describe_security_groups()['SecurityGroups'] if sg['GroupName'] == 'default'],
            Scheme='internet-facing',
            Type='application',
            IpAddressType='ipv4'
        )
        load_balancer_arn = load_balancer_response['LoadBalancers'][0]['LoadBalancerArn']
        print(f"Created Load Balancer: {load_balancer_arn}")

        elb_client.create_listener(
            LoadBalancerArn=load_balancer_arn,
            Protocol='HTTP',
            Port=80,
            DefaultActions=[{
                'Type': 'forward',
                'TargetGroupArn': target_group_arn
            }]
        )
        print("Listener created for Load Balancer.")

        return load_balancer_arn

    except Exception as e:
        print(f"An error occurred: {e}")

def create_launch_template(region_name, instance_id, template_name):
    ec2_client = boto3.client('ec2', region_name=region_name)

    try:
        instance = ec2_client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
        launch_template_response = ec2_client.create_launch_template(
            LaunchTemplateName=template_name,
            LaunchTemplateData={
                'ImageId': instance['ImageId'],
                'InstanceType': instance['InstanceType'],
                'SecurityGroupIds': [sg['GroupId'] for sg in instance['SecurityGroups']],
            }
        )
        launch_template_id = launch_template_response['LaunchTemplate']['LaunchTemplateId']
        print(f"Created Launch Template: {launch_template_id}")
        return launch_template_id

    except Exception as e:
        print(f"An error occurred while creating launch template: {e}")
        return None

def create_auto_scaling_group(region_name, launch_template_id):
    as_client = boto3.client('autoscaling', region_name=region_name)

    try:
        as_client.create_auto_scaling_group(
            AutoScalingGroupName='my-auto-scaling-group',
            LaunchTemplate={
                'LaunchTemplateId': launch_template_id,
                'Version': '$Latest'
            },
            MinSize=1,
            MaxSize=1,
            DesiredCapacity=1,
            VPCZoneIdentifier=','.join(
                [subnet['SubnetId'] for subnet in boto3.client('ec2', region_name=region_name).describe_subnets()['Subnets']]
            )
        )
        print("Auto Scaling group created successfully.")

    except Exception as e:
        print(f"An error occurred while creating the Auto Scaling group: {e}")

region = "us-east-1"  
no_of_Ins = input('Enter no of Instances to be created :')
createInstance(no_of_Ins)
instances = list_instances(region)

print("Waiting for instances to initialize...")
time.sleep(230)

template_name = input('Enter the template name :')
create_load_balancer(region, instances)
if instances:
    launch_template_id = create_launch_template(region, instances[0], template_name)

    if launch_template_id:
        create_auto_scaling_group(region, launch_template_id)
else:
    print("No running instances found to create an Auto Scaling group.")
