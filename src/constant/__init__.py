import os
from urllib.parse import quote_plus

AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "akshat"
MONGO_COLLECTION_NAME = "waferfault"


TARGET_COLUMN = "quality"
username = "vermaakshat628"
password = quote_plus("Ajtdmws@1")  # encodes the '@'

#url
MONGO_DB_URL= f"mongodb+srv://{username}:{password}@cluster0.kvdlevi.mongodb.net/?appName=Cluster0"


MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = "artifacts"
