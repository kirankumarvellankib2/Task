# test_file_uploader.py

import pytest
from unittest.mock import MagicMock
from file_uploader.s3_uploader import S3Uploader
from file_uploader.gcs_uploader import GCSUploader
from main_program import process_directory as FileHandler


@pytest.fixture
def mock_file_handler(mocker):
    return FileHandler(source_dir='/mock/source/dir',
                       s3_config={'access_key': 'access_key', 'secret_key': 'secret_key', 'region': 'region', 'bucket': 'bucket'},
                       gcs_config={'credentials_path': 'credentials_path', 'bucket': 'bucket'})

def test_process_files_calls_s3_uploader_for_images(mock_file_handler, mocker):
    mocker.patch('mymodule.file_handler.S3Uploader.upload')
    mock_file_handler.process_files(file_types={'images': ['image/jpeg']})
    assert S3Uploader.upload.called


def test_s3_uploader():
    s3_uploader = S3Uploader('access_key', 'secret_key', 'bucket_name', ['jpg'], [])
    s3_uploader.s3.upload_file = MagicMock()

    file_path = 'test.jpg'
    s3_uploader.upload_file(file_path)
    s3_uploader.s3.upload_file.assert_called_with(file_path, 'bucket_name', file_path)


def test_gcs_uploader():
    gcs_uploader = GCSUploader('credentials.json', 'bucket_name', ['pdf'])
    gcs_uploader.client.bucket = MagicMock()
    gcs_uploader.client.bucket.blob = MagicMock()

    file_path = 'test.pdf'
    gcs_uploader.upload_file(file_path)
    gcs_uploader.client.bucket.assert_called_with('bucket_name')
    gcs_uploader.client.bucket.blob.assert_called_with(file_path)

print ("test")

