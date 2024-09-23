from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
url="mongodb+srv://deepak:admin_dpk@cluster1.ounwm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

#create new client and connect to server
client = MongoClient(url)

#create a databse name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

df=pd.read_csv(r"D:\sensor\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

