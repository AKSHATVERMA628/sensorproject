from pymongo import MongoClient
import pandas as pd
import json
from urllib.parse import quote_plus


username = "vermaakshat628"
password = quote_plus("Ajtdmws@1")  # encodes the '@'

#url
uri = f"mongodb+srv://{username}:{password}@cluster0.kvdlevi.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)
print("✅ Connected successfully!")

from typing import Collection
# create database name and collection name
DATABASE_NAME="akshat"
COLLECTION_NAME="waferfault"

df=pd.read_csv("D:\sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)