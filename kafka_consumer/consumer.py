from kafka import KafkaConsumer
import time
import logging
import json
from elasticsearch import Elasticsearch


if __name__ == '__main__':
    index = 0
    client = Elasticsearch('elasticsearch:9200')

    consumer = KafkaConsumer('my-topic-example',
                             bootstrap_servers=['kafka:9093'])

    while True:
        for msg in consumer:
            print(f'[{index}] Received messaged: {msg.value.decode()}')

            elastic_msg = {'index': index, 'message': msg.value.decode()}
            res = client.index(index="my-topic-example", body=elastic_msg)

            index += 1

    # msg_pack = consumer.poll(500)
    # for tp, messages in msg_pack.items():
    #     print('Received ' + str(len(messages)) + " records")
    #     for message in messages:
            # res = client.index("'my-topic-example", message.value)
            # print(res['result'])

    # if len(msg_pack):
    #     logging.info("Committing Offset...")
    #     consumer.commit()
    #     logging.info("Committed Successfully")