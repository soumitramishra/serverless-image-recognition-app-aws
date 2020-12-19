import json
import boto3
import base64


def lambda_handler(event, context):
    try:
        # Put object to S3 bucket
        s3 = boto3.client('s3')
        bucket_name = 'original-widget-images-bucket'
        data = json.loads(event['body'])
        name = data['name']
        image = data['file']
        image = image[image.find(",") + 1:]
        dec = base64.b64decode(image + "===")
        s3.put_object(Bucket=bucket_name, Key=name, Body=dec)

        # Success Response
        response_object = {
            'statusCode': 200,
            'body': "image uploaded succesfully"
        }
    except Exception as e:
        # Failure Response
        response_object = {
            'statusCode': 200,
            'body': str(e)
        }
    return response_object
