import boto3

client = boto3.client('s3')

response = client.list_objects(Bucket='smir-yan-bucket')


for content in response['Contents']:
    obj_ = client.get_object(Bucket='smir-yan-bucket', Key=content['Key'])
    print(content['Key'], obj_['LastModified'])