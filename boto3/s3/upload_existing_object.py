import boto3

s3 = boto3.client('s3')
#with open('/home/ec2-user/environment/ekans/boto3/s3/test_text.txt', 'rb') as f:
#    s3.put_object(Bucket='dferguson-boto3-03032024', Key='test_text.txt', Body=f, ContentType='text/plain')
# above loads to memory

s3.upload_file('home/ec2-user/environment/ekans/boto3/s3/test_text.txt', 'dferguson-boto3-03032024', 'test_text_upload.txt', ExtraArgs={'ContentType':'text/plain'})