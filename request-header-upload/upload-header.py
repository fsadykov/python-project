from botocore.exceptions import ClientError
import requests
import boto3
import json
import boto3
import os

url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
file_name = "header.txt"
bucket_name = "marvel-scripting-assessment-bucket"

if os.environ.get("ACCESS_KEY") and os.environ.get("SECRET_KEY"):
    creds = {
        "aws_access_key_id" : os.environ.get("ACCESS_KEY"),
        "aws_secret_access_key" : os.environ.get("SECRET_KEY")
    }

else:
    print("Error: Can not find environment variables <ACCESS_KEY>, <SECRET_KEY>")
    exit()


def getHeaderLoadFile(url, file_name):
    """
    Function to get header and write to file
    """

    resp = requests.get(url)
    
    # checking for response code
    if resp.status_code == 200:

        # open the file write mode
        with open(file_name, 'w') as file:
            file.write(f"{resp.headers}")


def upload_file(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client(
        's3',
        aws_access_key_id=creds['aws_access_key_id'],
        aws_secret_access_key=creds['aws_secret_access_key'],
    )
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == '__main__':

    # getHeaderLoadFile should be called first
    getHeaderLoadFile(url, file_name)

    # upload_file function should be called after getHeaderLoadFile
    upload_file(file_name, bucket_name)
