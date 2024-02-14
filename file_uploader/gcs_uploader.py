# gcs_uploader

from google.cloud import storage


class GCSUploader:
    def __init__(self, credentials_path, bucket_name, allowed_document_types):
        self.client = storage.Client.from_service_account_json(credentials_path)
        self.bucket_name = bucket_name
        self.allowed_document_types = allowed_document_types

    def upload_file(self, file_path):
        #file upploader and file type
        file_type = file_path.split('.')[-1].lower()

        if file_type in self.allowed_document_types:
            try:
                bucket = self.client.bucket(self.bucket_name)
                blob = bucket.blob(file_path)
                blob.upload_from_filename(file_path)
                print(f"{file_path} uploaded to Google Cloud Storage")
            except Exception as e:
                print(f"Error uploading {file_path} to Google Cloud Storage: {e}")
