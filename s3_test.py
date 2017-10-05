import boto3
import os

region = 'リージョン'
IdentityPoolId = 'プールID'
bucket = 'バケット名'
key = 'key(パス)'

client = boto3.client('cognito-identity', region)

resp =  client.get_id(IdentityPoolId=identityPoolId)
# 1回目のアクセスでCognitoの認証IDを得る
print("\nIdentity ID: %s"%(resp['IdentityId']))
print("\nRequest ID: %s"%(resp['ResponseMetadata']['RequestId']))

# 2回目のアクセスでSessionを確立するための認証情報を得る
resp = client.get_credentials_for_identity(IdentityId=resp['IdentityId'])
secretKey = resp['Credentials']['SecretKey']
accessKey = resp['Credentials']['AccessKeyId']
token = resp['Credentials']['SessionToken']
print("\nToken: %s"%(token))
print("\nSecretKey: %s"%(secretKey))
print("\nAccessKey ID: %s"%(accessKey))
print("====================")
print(resp)

print("^^^^^^^^^^^^^^^^^^^^")
# 認証情報を用いて S3 Object にアクセスする
session = boto3.session.Session(
        aws_access_key_id=accessKey,
        aws_secret_access_key=secretKey,
        aws_session_token=token,
        region_name=region)
s3 = session.resource('s3')
obj = s3.Object(bucket_name=bucket, key=key)
print("******************")
# 以下は単純に読み込んで長さを返す例
response = obj.get()
data = response['Body'].read()
# ファイルに書き込み
saveData = open('.tmp_download', 'wb')
saveData.write(data)
saveData.close()

os.system('./imgcat .tmp_download')
