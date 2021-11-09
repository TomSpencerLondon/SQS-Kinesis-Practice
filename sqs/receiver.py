import boto3
import time

sqs = boto3.client('sqs')
''' :type : pyboto3.sqs '''

url = "https://sqs.eu-west-1.amazonaws.com/706054169063/orders"
running = True
while running:
    result = sqs.receive_message(QueueUrl=url, MaxNumberOfMessages=10)

    for message in result['Messages']:
        deleted = sqs.delete_message(QueueUrl=url, ReceiptHandle=message['ReceiptHandle'])
        print(deleted)
    time.sleep(1)