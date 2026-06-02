import json
import logging
import os
from typing import Any

from confluent_kafka import Producer

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "my-topic")

producer = Producer(
    {
        "bootstrap.servers": os.getenv(
            "KAFKA_BOOTSTRAP_SERVERS",
            "kafka-broker:29092",
        ),
        "client.id": os.getenv("HOSTNAME", "gateway-service"),
    },
)


def _delivery_report(err, msg) -> None:  # noqa: ANN001
    if err is not None:
        logging.warning("Failed to deliver statistics event to Kafka: %s", err)


def produce_statistics_event(event: dict[str, Any]) -> None:
    """Publish a statistics event directly from gateway to Kafka.

    Statistics collection must not depend on statistics-service availability.
    If Kafka is temporarily unavailable, the API request itself should still be returned
    to the user; the failure is only logged.
    """
    payload = json.dumps(event, ensure_ascii=False, default=str).encode("utf-8")

    try:
        producer.produce(
            KAFKA_TOPIC,
            value=payload,
            callback=_delivery_report,
        )
        producer.poll(0)
    except BufferError:
        # Local librdkafka queue is full. Give the producer a moment to deliver
        # already queued records and then retry once.
        producer.poll(1)
        producer.produce(
            KAFKA_TOPIC,
            value=payload,
            callback=_delivery_report,
        )
        producer.poll(0)
    except Exception as err:  # noqa: BLE001
        logging.warning("Kafka statistics producer error: %s", err)
