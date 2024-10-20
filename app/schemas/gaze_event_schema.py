from pydantic import BaseModel
from typing import List

class GazePoint(BaseModel):
    timestamp: float
    norm_pos: List[float]
    pupil_diameter: float

class GazeEvent(BaseModel):
    gazed_object: str
    gaze_activity: str
    gaze_points: List[GazePoint]