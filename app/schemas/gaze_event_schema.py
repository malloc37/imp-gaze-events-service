from pydantic import BaseModel

class GazeEvent(BaseModel):
    gazed_object: str
    gaze_activity: str