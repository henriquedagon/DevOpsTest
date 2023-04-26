from pymongo import MongoClient
import os

# Get MongoDB Client
def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username=os.environ.get('DB_USERNAME'), 
                         password=os.environ.get('DB_PASSWORD'),
                         authSource=os.environ.get('DB_AUTH_SOURCE'))
    
    db = client["animal_db"]
    return db
