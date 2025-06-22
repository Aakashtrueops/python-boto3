# import boto3
# client = boto3.client('s3, region_name='us-east-1')
# client.create_bucket(Bucket='Aakash-test0990')
# print($Bucket)
      

import boto3 # type: ignore
Bucketname = 'Aakash-test0990'
Regionname = 'us-east-1'

client = boto3.client('s3', region_name='Regionname')
client.create_bucket(
    Bucket='Bucketname'
)

print(f"'Bucketname' created successfully.")
