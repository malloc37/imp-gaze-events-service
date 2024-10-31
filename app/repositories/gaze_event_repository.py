from pymongo import MongoClient
from app.config import MONGO_URI
import logging

client = MongoClient(MONGO_URI)
mongo = client.gaze_data_db

logger = logging.getLogger(__name__)

class GazeEventRepository:
    def __init__(self):
        self.gaze_events = mongo.get_collection('gaze_events')

    def save_gaze_event(self, gaze_event: dict):
        """Insert gaze event into MongoDB."""
        try:
            result = self.gaze_events.insert_one(gaze_event)
            if result.inserted_id:
                logger.info(f"Gaze event inserted with id: {result.inserted_id}")
                return result.inserted_id
            else:
                logger.error("Failed to insert gaze event")
                return None
        except Exception as e:
            logger.error(f"Error while inserting gaze event: {e}")
            return None