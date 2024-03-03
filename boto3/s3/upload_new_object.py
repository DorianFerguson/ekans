import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket='dferguson-boto3-03032024', Key='test_text_string.txt', Body='Welcome to boto3!', ContentType='text/plain')
