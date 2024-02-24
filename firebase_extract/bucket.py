# scheme_edesia/storage/bucket_operations.py

from google.cloud import storage as gcloud_storage
from google.oauth2 import service_account
import os

def download_all_files(service_account_path, bucket_name):
    gcs_credentials = service_account.Credentials.from_service_account_file(service_account_path)
    gcs_client = gcloud_storage.Client(credentials=gcs_credentials, project=gcs_credentials.project_id)
    bucket = gcs_client.get_bucket(bucket_name)

    local_dir = './firebase_storage_files'
    os.makedirs(local_dir, exist_ok=True)

    blobs = bucket.list_blobs()
    for blob in blobs:
        if not blob.name.endswith('/'):
            local_file_path = os.path.join(local_dir, blob.name)
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            blob.download_to_filename(local_file_path)
            print(f'Downloaded {blob.name} to {local_file_path}')
