from kafka import KafkaProducer
import time
import random
from json import dumps


if __name__ == '__main__':
    index = 0

    while True:
        message = str(random.random())
        # producer = KafkaProducer(bootstrap_servers='kafka:9093')
        producer = KafkaProducer(bootstrap_servers=['kafka:9093'],
                                 acks='all',  # Required for safe producer
                                 retries=999999999999,  # Required for safe producer
                                 max_in_flight_requests_per_connection=5,  # Required for safe producer
                                 linger_ms=20,  # Required for high throughput producer
                                 batch_size=32 * 1024)  # Required for high throughput producer
        print(f"[{index}] Sending message: {message}")
        producer.send('my-topic-example', message.encode())
        producer.flush()

        index += 1
        time.sleep(1)