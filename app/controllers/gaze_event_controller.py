from fastapi import APIRouter, HTTPException
import logging
from app.schemas.gaze_event_schema import GazeEvent
from app.services.gaze_event_service import GazeEventService

router = APIRouter()
service = GazeEventService()

logger = logging.getLogger(__name__)

@router.post("/gaze_event/")
async def create_gaze_event(gaze_event: GazeEvent):
    logger.info("Received new gaze event data")
    try:
        # Convert gaze event to dictionary
        gaze_event_data = gaze_event.dict()

        # For each gaze point, add gazed_object and gaze_activity to the dictionary
        for gaze_point in gaze_event_data['gaze_points']:
            gaze_point['gazed_object'] = gaze_event.gazed_object
            gaze_point['gaze_activity'] = gaze_event.gaze_activity

        # Save event and publish to Kafka
        service.save_gaze_event(gaze_event_data)
        logger.info("Gaze event saved successfully")

        return {"message": "Gaze event saved successfully."}
    except Exception as e:
        logger.error(f"Error while processing gaze event: {e}")
        raise HTTPException(status_code=500, detail=str(e))