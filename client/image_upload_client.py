import base64
import requests
import json

# image file to open
image_file = open("../macbook.jpg", "rb")
encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# URL for S3 bucket
url = "https://vg1g2597w9.execute-api.us-east-1.amazonaws.com/prod/upload-image-s3-function"

payload = {
     "name" : "macbook27.jpg",
     "file": encoded_string
}

# Uploading
headers = {'content-type': 'application/json'}
response = requests.post( url, data=json.dumps(payload), headers=headers)
print(response.content)