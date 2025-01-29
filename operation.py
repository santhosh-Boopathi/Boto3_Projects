import boto3
import requests
import json
from botocore.exceptions import NoCredentialsError
from variables import AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME, BUCKET_NAME, URL_TO_SCRAPE

def create_bucket_if_not_exists():
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=REGION_NAME)
    existing_buckets = [bucket['Name'] for bucket in s3.list_buckets()['Buckets']]
    
    if BUCKET_NAME not in existing_buckets:
        if REGION_NAME == 'us-east-1':
            s3.create_bucket(Bucket=BUCKET_NAME)
        else:
            s3.create_bucket(Bucket=BUCKET_NAME, CreateBucketConfiguration={'LocationConstraint': REGION_NAME})
        print(f'Bucket {BUCKET_NAME} created.')
    else:
        print(f'Bucket {BUCKET_NAME} already exists.')

def upload_index_html():
    response = requests.get(URL_TO_SCRAPE)
    with open('index.html', 'w') as file:
        file.write(response.text)
    
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=REGION_NAME)
    
    # Upload the file
    s3.upload_file('index.html', BUCKET_NAME, 'index.html', ExtraArgs={'ContentType': 'text/html'})
    
    # Enable static website hosting
    s3.put_bucket_website(Bucket=BUCKET_NAME, WebsiteConfiguration={'IndexDocument': {'Suffix': 'index.html'}})
    
    # Set bucket policy to allow public access
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
            }
        ]
    }

    s3.put_bucket_policy(Bucket=BUCKET_NAME, Policy=json.dumps(bucket_policy))
    
    print('index.html uploaded, static website hosting enabled, and public access granted.')
