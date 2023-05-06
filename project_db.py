from pymongo import MongoClient
import config

Database =config.DATABASE
port = config.mongodb_port

uri = (f"mongodb://localhost:{port}/")

mongo_db_client = MongoClient(uri)

db = mongo_db_client[Database]

collection_user = db['Student_details']
