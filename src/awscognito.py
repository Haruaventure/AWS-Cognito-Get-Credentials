import boto3

region = 'us-east-1'
identity_pool = '__Identity_Pool_ID__'

client = boto3.client('cognito-identity', region_name=region)
_id = client.get_id(IdentityPoolId=identity_pool)
_id = _id['IdentityId']

credentials = client.get_credentials_for_identity(IdentityId=_id)

access_key = credentials['Credentials']['AccessKeyId']
secret_key = credentials['Credentials']['SecretKey']
session_token = credentials['Credentials']['SessionToken']
identity_id = credentials['IdentityId']

print("Access Key : " + access_key)
print("Secret Key : " + secret_key)
print("Session Token : " + session_token)
print("Identity Id : " + identity_id)
