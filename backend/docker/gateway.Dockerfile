FROM python:3.10-slim-buster

WORKDIR /gateway

COPY ./gateway_service /gateway
COPY ../config.yaml /gateway
COPY ../requirements_kafka.txt /gateway

RUN pip3.10 install -r requirements_kafka.txt

EXPOSE 8080

CMD ["python3", "app/main.py"]
