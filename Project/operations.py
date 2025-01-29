# import boto3, requests, json
# from variable import file_path
# from botocore.exceptions import ClientError

# def upload_file(bucket_name):
#     object_name = "index.html"  
#     s3_client = boto3.client('s3')
#     try:
#         s3_client.upload_file(
#             Filename=file_path,
#             Bucket=bucket_name,
#             Key="index.html",
#             ExtraArgs={"ContentType": "text/html"}
#         )
#         print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{object_name}' with public access.")
#     except ClientError as e:
#         print(f"Error uploading file or setting public access: {e}")

# def public_access_disable(bucket_name):
#     s3_client = boto3.client('s3')
#     s3_client.put_public_access_block(
#             Bucket=bucket_name,
#             PublicAccessBlockConfiguration={
#                 "BlockPublicAcls": False,
#                 "IgnorePublicAcls": False,
#                 "BlockPublicPolicy": False,
#                 "RestrictPublicBuckets": False
#             }
#         )
#     print("Public access block disabled for the bucket.")

# def bucket_policy(bucket_name):
#     s3_client = boto3.client('s3')
#     bucket_policy = {
#             "Version": "2012-10-17",
#             "Statement": [
#                 {
#                     "Effect": "Allow",
#                     "Principal": "*",
#                     "Action": "s3:GetObject",
#                     "Resource": f"arn:aws:s3:::{bucket_name}/*"
#                 }
#             ]
#         }
#     s3_client.put_bucket_policy(
#             Bucket=bucket_name,
#             Policy=json.dumps(bucket_policy)
#         )
#     print("Bucket policy applied for public read access.")

# def static_website_hosting(bucket_name):
#     region = "us-east-1"
#     s3_client = boto3.client('s3')
#     public_access_disable(bucket_name)
#     upload_file(bucket_name)
#     s3_client.put_bucket_website(
#             Bucket=bucket_name,
#             WebsiteConfiguration={
#                 'IndexDocument': {'Suffix': 'index.html'},
#             }
#         )
#     print(f"Static website hosting enabled on bucket '{bucket_name}'.")
#     bucket_policy(bucket_name)
#     website_endpoint = f"http://{bucket_name}.s3-website-{region}.amazonaws.com"
#     print(f"Your website is hosted at: {website_endpoint}")

    

# def scraping_website():
#     url = input("Enter the valid website url: ")
#     try:
#         response = requests.get(url)
#         response.raise_for_status() 
#         with open("index.html", 'w', encoding='utf-8') as file:
#             file.write(response.text)
#         print(f"HTML content of {url} has been saved to index.html")
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching the webpage: {e}")


# def create_bucket():
#     region = "us-east-1"
#     bucket_name = input("Enter unique Bucket name:")
#     s3_client = boto3.client('s3', region_name=region)
#     response = s3_client.create_bucket(Bucket=bucket_name)
#     print(f"Bucket '{bucket_name}' created successfully.")
    

# def listing_buckets():
#     s3 = boto3.client('s3')
#     response = s3.list_buckets()
#     if not response['Buckets']:
#         print("There are no buckets")
#         create_bucket()
#         scraping_website()    
#         first_bucket_name = response['Buckets'][0]['Name']
#         print(first_bucket_name)
#         static_website_hosting(first_bucket_name)
#     else:
#         scraping_website()    
#         first_bucket_name = response['Buckets'][0]['Name']
#         print(first_bucket_name)
#         static_website_hosting(first_bucket_name)

# import boto3
# import requests
# import json
# import os
# from botocore.exceptions import ClientError
# from variable import file_path  # Ensure the file_path is correctly defined here

# def upload_file(bucket_name, file_path):
#     object_name = "index.html"  
#     s3_client = boto3.client('s3')
#     try:
#         # Make sure the file exists before attempting to upload
#         if os.path.exists(file_path):
#             s3_client.upload_file(
#                 Filename=file_path,
#                 Bucket=bucket_name,
#                 Key="index.html",
#                 ExtraArgs={"ContentType": "text/html"}
#             )
#             print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{object_name}' with public access.")
#         else:
#             print(f"Error: The file '{file_path}' does not exist.")
#     except ClientError as e:
#         print(f"Error uploading file or setting public access: {e}")

# def public_access_disable(bucket_name):
#     s3_client = boto3.client('s3')
#     s3_client.put_public_access_block(
#             Bucket=bucket_name,
#             PublicAccessBlockConfiguration={
#                 "BlockPublicAcls": False,
#                 "IgnorePublicAcls": False,
#                 "BlockPublicPolicy": False,
#                 "RestrictPublicBuckets": False
#             }
#         )
#     print("Public access block disabled for the bucket.")

# def bucket_policy(bucket_name):
#     s3_client = boto3.client('s3')
#     bucket_policy = {
#             "Version": "2012-10-17",
#             "Statement": [
#                 {
#                     "Effect": "Allow",
#                     "Principal": "*",
#                     "Action": "s3:GetObject",
#                     "Resource": f"arn:aws:s3:::{bucket_name}/*"
#                 }
#             ]
#         }
#     s3_client.put_bucket_policy(
#             Bucket=bucket_name,
#             Policy=json.dumps(bucket_policy)
#         )
#     print("Bucket policy applied for public read access.")

# def static_website_hosting(bucket_name, file_path):
#     region = "us-east-1"
#     s3_client = boto3.client('s3')
#     public_access_disable(bucket_name)
#     upload_file(bucket_name, file_path)
#     s3_client.put_bucket_website(
#             Bucket=bucket_name,
#             WebsiteConfiguration={
#                 'IndexDocument': {'Suffix': 'index.html'},
#             }
#         )
#     print(f"Static website hosting enabled on bucket '{bucket_name}'.")
#     bucket_policy(bucket_name)
#     website_endpoint = f"http://{bucket_name}.s3-website-{region}.amazonaws.com"
#     print(f"Your website is hosted at: {website_endpoint}")

# def scraping_website():
#     url = input("Enter the valid website url: ")
#     try:
#         response = requests.get(url)
#         response.raise_for_status() 
#         with open("index.html", 'w', encoding='utf-8') as file:
#             file.write(response.text)
#         print(f"HTML content of {url} has been saved to index.html")
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching the webpage: {e}")

# def create_bucket():
#     region = "us-east-1"
#     bucket_name = input("Enter unique Bucket name: ")
#     s3_client = boto3.client('s3', region_name=region)
#     response = s3_client.create_bucket(Bucket=bucket_name)
#     print(f"Bucket '{bucket_name}' created successfully.")

# def listing_buckets():
#     s3 = boto3.client('s3')
#     response = s3.list_buckets()
    
#     if not response.get('Buckets', []):  # Check if there are no buckets
#         print("There are no buckets")
#         create_bucket()
#         scraping_website()    
#         # After creating the bucket, list buckets again to ensure it's available
#         response = s3.list_buckets()  # Re-fetch the list of buckets
#         first_bucket_name = response['Buckets'][0]['Name']
#         print(f"First bucket name: {first_bucket_name}")
#         static_website_hosting(first_bucket_name, "index.html")  # Pass correct file_path here
#     else:
#         scraping_website()    
#         first_bucket_name = response['Buckets'][0]['Name']
#         print(f"First bucket name: {first_bucket_name}")
#         static_website_hosting(first_bucket_name, "index.html")  # Pass correct file_path here

# if __name__ == "__main__":
#     listing_buckets()



import boto3
import requests
import json
import os
from botocore.exceptions import ClientError
from variable import file_path  # Ensure the file_path is correctly defined here

def upload_file(bucket_name, file_path):
    object_name = "index.html"  
    s3_client = boto3.client('s3')
    try:
        # Make sure the file exists before attempting to upload
        if os.path.exists(file_path):
            s3_client.upload_file(
                Filename=file_path,
                Bucket=bucket_name,
                Key="index.html",
                ExtraArgs={"ContentType": "text/html"}
            )
            print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{object_name}' with public access.")
        else:
            print(f"Error: The file '{file_path}' does not exist.")
    except ClientError as e:
        print(f"Error uploading file or setting public access: {e}")

def public_access_disable(bucket_name):
    s3_client = boto3.client('s3')
    s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                "BlockPublicAcls": False,
                "IgnorePublicAcls": False,
                "BlockPublicPolicy": False,
                "RestrictPublicBuckets": False
            }
        )
    print("Public access block disabled for the bucket.")

def bucket_policy(bucket_name):
    s3_client = boto3.client('s3')
    bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": f"arn:aws:s3:::{bucket_name}/*"
                }
            ]
        }
    s3_client.put_bucket_policy(
            Bucket=bucket_name,
            Policy=json.dumps(bucket_policy)
        )
    print("Bucket policy applied for public read access.")

def static_website_hosting(bucket_name, file_path):
    region = "us-east-1"
    s3_client = boto3.client('s3')
    public_access_disable(bucket_name)
    upload_file(bucket_name, file_path)
    s3_client.put_bucket_website(
            Bucket=bucket_name,
            WebsiteConfiguration={
                'IndexDocument': {'Suffix': 'index.html'},
            }
        )
    print(f"Static website hosting enabled on bucket '{bucket_name}'.")
    bucket_policy(bucket_name)
    website_endpoint = f"http://{bucket_name}.s3-website-{region}.amazonaws.com"
    print(f"Your website is hosted at: {website_endpoint}")

def scraping_website():
    url = input("Enter the valid website url: ")
    try:
        response = requests.get(url)
        response.raise_for_status() 
        with open("index.html", 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"HTML content of {url} has been saved to index.html")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")

def create_bucket():
    region = "us-east-1"
    bucket_name = input("Enter unique Bucket name: ")
    s3_client = boto3.client('s3', region_name=region)
    response = s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")

def listing_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    
    if not response.get('Buckets', []):  # Check if there are no buckets
        print("There are no buckets")
        create_bucket()
        scraping_website()    
        # After creating the bucket, list buckets again to ensure it's available
        response = s3.list_buckets()  # Re-fetch the list of buckets
        first_bucket_name = response['Buckets'][0]['Name']
        print(f"First bucket name: {first_bucket_name}")
        static_website_hosting(first_bucket_name, "index.html")  # Pass correct file_path here
    else:
        # If buckets exist, list them
        print("Existing buckets:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")
        
        scraping_website()    
        first_bucket_name = response['Buckets'][0]['Name']
        print(f"First bucket name: {first_bucket_name}")
        static_website_hosting(first_bucket_name, "index.html")  # Pass correct file_path here

