from kafka import KafkaProducer
import json
import time

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC_NAME = 'logs'

def main():
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    i = 0
    while True:
        message = {TOPIC_NAME: f'Producer TWO {i}'}
        producer.send(TOPIC_NAME, value=message)
        i += 1
        time.sleep(.5)

if __name__ == "__main__":
    main()
