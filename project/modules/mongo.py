from pymongo import MongoClient
from decouple import config

DBPASSW = config("DBPASSW")

def connect():
  try:
    #connect to the cluster
    client = MongoClient(f"mongodb+srv://adminu:{DBPASSW}@cluster0.4jfcf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.shortener
    return db

  except Exception as e:
    print(e)