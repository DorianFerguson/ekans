import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='dferguson-boto3-03032024'
)

print(response)