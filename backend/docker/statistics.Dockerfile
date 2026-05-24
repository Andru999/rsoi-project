FROM python:3.10-slim-buster

WORKDIR /statistics

COPY ./statistics_service /statistics
COPY ../config.yaml /statistics
COPY ../requirements_kafka.txt /statistics

RUN pip3.10 install -r requirements_kafka.txt

EXPOSE 8090

CMD ["python3", "app/main.py"]
