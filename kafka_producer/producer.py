from kafka import KafkaProducer
import time
import random
from config import logger_config
from json import dumps
import logging
from logging.config import dictConfig

dictConfig(config=logger_config)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    index = 0

    producer = KafkaProducer(bootstrap_servers=['kafka:9093'],
                             acks='all',
                             retries=999999999999)

    while True:
        message = 'EXAMPLE MESSAGE TEST'

        logger.warning(f"[{index}] Sending message !!!")
        producer.send('my-topic', message.encode())
        producer.flush()

        index += 1
        time.sleep(1)
