import boto3

 # s3 = boto3.client('s3')

# response = s3.list_objects_v2(Bucket='dferguson-boto3-03032024')
#print(response)
#use JSON formatter to read response and find what you're looking for

# extention = 'txt'

# iterate for desired info
# for content in response['Contents']:
#    if (extention in content['Key'][-(len(extention)):]):
    #using some ingenuity to parse for file types
    # as boto3 does not do this natively
#        print(content['Key'])
    

# response = s3.list_objects_v2(Bucket='dferguson-boto3-03032024', Prefix='folders/folder_a')
#use prefixes to narrow list to specified location

# ===== let's make it a function ===========

def filter_object_extension(client, bucket, extension):
    keys = []
    response = s3.list_objects_v2(Bucket=bucket)
    for content in response['Contents']:
        if (extension in content['Key'][-(len(extension)):]):
            keys.append(content['Key'])
    return keys
    
def filter_object_keys(client, bucket, prefix=''):
    keys = []
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response['Contents']:
        keys.append(content['Key'])
    return keys

s3 = boto3.client('s3')

response = filter_object_extension(s3, 'dferguson-boto3-03032024', '.txt')
print(response)

response = filter_object_keys(s3, 'dferguson-boto3-03032024')
print(response)