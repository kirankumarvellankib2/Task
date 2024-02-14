# file_uploader/s3_uploader.py

import boto3
from botocore.exceptions import NoCredentialsError


class S3Uploader:
    def __init__(self, access_key, secret_key, bucket_name, allowed_image_types, allowed_media_types):
        self.s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        self.bucket_name = bucket_name
        self.allowed_image_types = allowed_image_types
        self.allowed_media_types = allowed_media_types

    def upload_file(self, file_path):
        #file uploader and file type 
        file_type = file_path.split('.')[-1].lower()

        if file_type in self.allowed_image_types or file_type in self.allowed_media_types:
            try:
                self.s3.upload_file(file_path, self.bucket_name, file_path)
                print(f"{file_path} uploaded to S3")
            except NoCredentialsError:
                print("Credentials not available")
