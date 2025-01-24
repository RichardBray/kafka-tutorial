from kafka import KafkaConsumer
import json

consumer_two = KafkaConsumer(
    'logs',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest'
)

for message in consumer_two:
    print(f"Received message: {message.value}")
