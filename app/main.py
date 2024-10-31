from fastapi import FastAPI
from app.controllers import gaze_event_controller
import logging

app = FastAPI()

app.include_router(gaze_event_controller.router)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Gaze Event API!"}