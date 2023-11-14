import os
from minio import Minio
from minio.error import S3Error
from pymongo import MongoClient

# MinIO configuration
minio_endpoint = "localhost:9000"  # Replace with your MinIO endpoint
access_key = "ilulale"
secret_key = "kstar101"
bucket_name = "davidpark"

# MongoDB configuration
mongo_uri = "mongodb://localhost:27017/"  # Replace with your MongoDB URI
mongo_db_name = "minio_files"
mongo_collection_name = "files"

# Initialize MinIO client
minio_client = Minio(
    minio_endpoint,
    access_key=access_key,
    secret_key=secret_key,
    secure=False  # Change to True if using HTTPS
)

# Initialize MongoDB client and database
mongo_client = MongoClient(mongo_uri)
mongo_db = mongo_client[mongo_db_name]
mongo_collection = mongo_db[mongo_collection_name]

def upload_to_minio(local_path, minio_path):
    try:
        minio_client.fput_object(bucket_name, minio_path, local_path)
        print(f"Uploaded {local_path} to {minio_path}")
    except S3Error as e:
        print(f"Error uploading {local_path}: {e}")

def insert_into_mongodb(file_name, minio_path):
    mongo_collection.insert_one({"file_name": file_name, "minio_path": minio_path})
    print(f"Inserted {file_name} into MongoDB")

def upload_folder_to_minio_and_mongodb(folder_path, minio_prefix=""):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            local_path = os.path.join(root, file_name)
            minio_path = os.path.join(minio_prefix, file_name)

            upload_to_minio(local_path, minio_path)
            insert_into_mongodb(file_name, minio_path)

if __name__ == "__main__":
    folder_to_upload = "./reels/"
    minio_prefix = "videos"  # Optional: Prefix to organize files in MinIO

    upload_folder_to_minio_and_mongodb(folder_to_upload, minio_prefix)
