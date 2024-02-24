from firebase_extract.admin import initialize_firebase_admin
from firebase_extract.realtime_db import backup_and_parse_realtime_db
from firebase_extract.bucket import download_all_files
from firebase_extract.firestore import backup_firestore

def main():
    # Initialize Firebase Admin with common credentials
    json_credentials_path = 'admin-sdk/[filename.json]' # add your credentials file path
    databaseURL = 'https://example.firebaseio.com'
    storageBucket = 'example.appspot.com'

    # Initialize Firebase Admin
    initialize_firebase_admin(json_credentials_path, databaseURL=databaseURL, storageBucket=storageBucket)

    # Backup and parse Realtime Database
    print("Backing up and parsing Realtime Database...")
    parsed_food_trucks = backup_and_parse_realtime_db()

    # Download all files from the Storage Bucket
    print("Downloading all files from the Storage Bucket...")
    download_all_files(json_credentials_path, storageBucket)

    # Backup Firestore Database
    print("Backing up Firestore Database...")
    backup_firestore()
    print("Firestore backup completed successfully.")

if __name__ == "__main__":
    main()
