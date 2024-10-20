
from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)

mongo = client.gaze_data_db