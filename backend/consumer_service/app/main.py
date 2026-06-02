import json
import logging
import os
import time

from confluent_kafka import Consumer, KafkaError
from models.statistics import StatisticsModel
from utils.database import get_session

logging.basicConfig(level=logging.DEBUG)

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "my-topic")

conf = {
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka-broker:29092"),
    "auto.offset.reset": "earliest",
    "enable.auto.commit": False,
    "group.id": os.getenv("KAFKA_GROUP_ID", "my-group"),
}


def consume_messages() -> None:
    consumer = Consumer(conf)
    consumer.subscribe([KAFKA_TOPIC])

    try:
        while True:
            msg = consumer.poll(timeout=30)
            logging.info("Polling")
            logging.info(msg)

            if msg is None:
                logging.info("No message")
                continue

            if msg.error():
                logging.info("Error")
                if msg.error().code() == KafkaError._PARTITION_EOF:  # noqa: SLF001
                    print(
                        f"Reached end of partition: {msg.topic()}[{msg.partition()}]",  # noqa: E501
                    )
                else:
                    print(f"Error while consuming messages: {msg.error()}")
                    logging.info(msg.error())
            else:
                data = msg.value().decode("utf-8")
                data_dict = json.loads(data)

                statistics = StatisticsModel(**data_dict)

                db = get_session()
                try:
                    db.add(statistics)
                    db.commit()
                    db.refresh(statistics)
                    consumer.commit(message=msg, asynchronous=False)
                finally:
                    db.close()

                print(f"Received message: {msg.value().decode('utf-8')}")
                logging.info(msg.value().decode("utf-8"))

    except Exception as e:
        print(f"Exception occurred while consuming messages: {e}")
        logging.info(e)
    finally:
        consumer.close()
        logging.info("Consumer closed")


def startup() -> None:
    logging.info("Starting consumer...")
    time.sleep(10)
    consume_messages()


if __name__ == "__main__":
    try:
        startup()
    except Exception as e:
        print(f"Exception occurred: {e}")
