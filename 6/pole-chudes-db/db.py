from pymongo import MongoClient

MONGO_URI = "mongodb://student:student123@localhost:27017/"
DB_NAME = "pole_chudes_db"

def get_collection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db["words"]