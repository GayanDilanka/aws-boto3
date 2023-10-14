
import boto3
import time

#Create ec2 client
ec2 = boto3.client('ec2')
response = ec2.describe_instances()

# #Print Reservations 
# print("--------------------------")
# print(response['Reservations'])
# print("--------------------------")

# #print the fist EC2 instance
# instance_id = response["Reservations"][0]["Instances"][0]["InstanceId"]
# print(instance_id) 


#loop through the reservations
for reservation in response["Reservations"]:
    
    #filter the instance data
    instance_id = reservation["Instances"][0]["InstanceId"]
    status_code = reservation["Instances"][0]["State"]["Code"]
    status = reservation["Instances"][0]["State"]["Name"]

    print("=========================")
    print(instance_id +" "+ status)
    
    #check the instance status send stop request if running
    if status_code == 16 :
        print("This instance is currently running..,Sending Stop request")
        response = ec2.stop_instances(
            InstanceIds=[
                instance_id,
            ],
        )
        # check the stop request response
        if response['StoppingInstances'][0]['CurrentState']['Code'] == 64:
            print("Stop request sent Success")
        else:
            print("Stop request failed")
    time.sleep(3)

