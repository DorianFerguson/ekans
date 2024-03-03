import boto3
# Make sure to install boto3 in enviroment pip or pip3 boto3

s3 = boto3.client('s3', aws_access_key_id="", aws_secret_key_id="", aws_session_token="")
# access can be given by using roles, aws configure or directly when calling the client

# MAIN 3 boto3 Interfaces, Session, Client, and Resource.
session = boto3.session()
# can directly pass in keys in order to make a single conection,
# typically a starting point. Can call client and resource
# directly from session

s3 = boto3.client('s3') # low level interface that allows direct access to aws 
# using api like methods
s3 = session.client('s3') # ditto ^. Note these can be called directly from boto3
# as well as from session
# gives full control over responses and the ability to parse them


s3 = boto3.resource('s3') # Higher level interface than client. returns similar things to
# python classes and interactable objects
s3 = session.rource('s3')

# client = API like responses resource = pythion like responses