import json
import logging
import time

from confluent_kafka import Consumer, KafkaError
from models.statistics import StatisticsModel
from utils.database import get_session

logging.basicConfig(level=logging.DEBUG)

conf = {
    "bootstrap.servers": "kafka:29092",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": True,
    "group.id": "my-group",
    "api.version.request": True,
    "api.version.fallback.ms": 0,
}


def consume_messages() -> None:
    consumer = Consumer(conf)
    consumer.subscribe(["my-topic"])

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
                db.add(statistics)
                db.commit()
                db.refresh(statistics)

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
