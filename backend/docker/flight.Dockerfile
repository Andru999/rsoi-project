FROM python:3.10-alpine

WORKDIR /flight

COPY ./flight_service /flight
COPY ../config.yaml /flight
COPY ../requirements.txt /flight

RUN pip3.10 install -r requirements.txt

EXPOSE 8060

CMD ["python3", "app/main.py"]
