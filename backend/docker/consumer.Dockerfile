FROM python:3.10-slim-buster

WORKDIR /consumer

COPY ./consumer_service /consumer
COPY ../config.yaml /consumer
COPY ../requirements_kafka.txt /consumer

RUN pip3.10 install -r requirements_kafka.txt

CMD ["python3", "app/main.py"]
