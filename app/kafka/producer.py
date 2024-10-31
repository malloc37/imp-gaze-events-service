from kafka import KafkaProducer
import json
from app.config import KAFKA_BOOTSTRAP_SERVERS
import logging

logger = logging.getLogger(__name__)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_event(topic, data):
    """Publish data to Kafka topic."""
    try:
        logger.info(f"Publishing event to Kafka topic {topic}: {data}")
        producer.send(topic, value=data)
        producer.flush()
    except Exception as e:
        logger.error(f"Failed to publish event to Kafka topic {topic}: {e}")