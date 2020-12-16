import json
import boto3
import base64

# This lambda function is used to upload an image which has to be inspected to the S3 bucket
def lambda_handler(event, context):
    try:
        s3 = boto3.client('s3')
        bucket_name = 'inspection-images-bucket'
        data = json.loads(event['body'])
        name = data['name']
        image = data['file']
        image = image[image.find(",") + 1:]
        dec = base64.b64decode(image + "===")
        s3.put_object(Bucket=bucket_name, Key=name, Body=dec)
        response_object = {
            'statusCode': 200,
            'body': "hello"
        }
    except Exception as e:
        response_object = {
            'statusCode': 200,
            'body': str(e)
        }
    return response_object