from kafka import KafkaProducer
import json
import time

TOPIC_NAME = 'logs'

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

i = 0
while True:
    message = {TOPIC_NAME: f'Producer ONE {i}'}
    producer.send(TOPIC_NAME, value=message)
    i += 1
    time.sleep(1)
