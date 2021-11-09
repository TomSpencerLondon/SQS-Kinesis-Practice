import boto3
import time

sqs = boto3.client('sqs')
''' :type : pyboto3.sqs '''

count = 0
running = True
while running:
    sqs.send_message(MessageBody="hello", QueueUrl="https://sqs.eu-west-1.amazonaws.com/706054169063/orders")
    count += 1
    print(count)
    time.sleep(1)
