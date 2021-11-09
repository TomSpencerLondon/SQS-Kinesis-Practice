import boto3
import time

firehose = boto3.client('firehose')
''' :type : pyboto3.firehose '''

count = 0
running = True
while running:
    firehose.put_record(DeliveryStreamName="PUT-S3-A10AQ", Record={
        "Data": f'hello from tom {time.time()}\n'
    })
    count += 1
    print(count)
    time.sleep(1)
