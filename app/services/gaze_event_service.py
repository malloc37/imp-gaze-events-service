from app.repositories.gaze_event_repository import GazeEventRepository
from app.kafka.producer import send_event
import logging

logger = logging.getLogger(__name__)


class GazeEventService:
    def __init__(self):
        self.repository = GazeEventRepository()

    def save_gaze_event(self, gaze_event_data):
        """Save gaze event to MongoDB and publish to Kafka."""
        # Save event to MongoDB
        inserted_id = self.repository.save_gaze_event(gaze_event_data)

        if inserted_id:
            gaze_event_data['_id'] = str(inserted_id)

            # If insert was successful, send to Kafka
            logger.info(f"Publishing event with id: {inserted_id} to Kafka")
            send_event("gaze_events", gaze_event_data)
        else:
            logger.error("Failed to save gaze event, not publishing to Kafka")