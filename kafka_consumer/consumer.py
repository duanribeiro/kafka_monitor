from kafka import KafkaConsumer
import time
import logging
import json
from elasticsearch import Elasticsearch
from config import logger_config
from logging.config import dictConfig

dictConfig(config=logger_config)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # client = Elasticsearch('elasticsearch:9200')
    consumer = KafkaConsumer('my-topic', bootstrap_servers=['kafka:9093'])

    index = 0
    while True:
        for msg in consumer:
            logger.warning(f'[{index}] Received messaged: {msg.value.decode()}')

            # elastic_msg = {'index': index, 'message': msg.value.decode()}
            # res = client.index(index="my-topic", body=elastic_msg, doc_type='example', id=index)

            index += 1