from pymongo import MongoClient
import os

# Get MongoDB Client
def get_db():
    client = MongoClient(host=os.environ.get('DB_HOST'),
                         username=os.environ.get('DB_USERNAME'), 
                         password=os.environ.get('DB_PASSWORD'),
                         authSource=os.environ.get('DB_AUTH_SOURCE'),
                         port=27017)

    db = client["animal_db"]
    return db
