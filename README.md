# imp-gaze-events-service
REST API which has a POST interface to send gaze events to `gaze_events`topic to the Kafka Broker at `130.82.171.231:9092`

## How to run
1. Install the requirements with `pip install -r requirements.txt`
2. Connect to the VPN (so that you can access the Kafka Broker)
3. Run `uvicorn app.main:app --reload` to start the server