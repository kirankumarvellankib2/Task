#main program
from file_uploader import S3Uploader, GCSUploader
import os

# Configurations
AWS_ACCESS_KEY = 'AWS access key'
AWS_SECRET_KEY = 'AWS Secret key'
AWS_BUCKET_NAME = 'Bucket name'
ALLOWED_IMAGE_TYPES = ['jpg', 'png', 'svg', 'webp']
ALLOWED_MEDIA_TYPES = ['mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm']

GCS_CREDENTIALS_PATH = "GCS credientials file path in json format"
GCS_BUCKET_NAME = 'My First Project'
ALLOWED_DOCUMENT_TYPES = ['doc', 'docx', 'csv', 'pdf', 'xls']

# main program to handle the file path and uploader
def process_directory(directory_path):
    s3_uploader = S3Uploader(AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, ALLOWED_IMAGE_TYPES, ALLOWED_MEDIA_TYPES)
    gcs_uploader = GCSUploader(GCS_CREDENTIALS_PATH, GCS_BUCKET_NAME, ALLOWED_DOCUMENT_TYPES)

    #extract the uploaded files and call the televent services.
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                s3_uploader.upload_file(file_path)
                gcs_uploader.upload_file(file_path)

if __name__ == "__main__":
    # File or directory path to call the function
    directory_to_process = "file/directory/path"
    process_directory(directory_to_process)
