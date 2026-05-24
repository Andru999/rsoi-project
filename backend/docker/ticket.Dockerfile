FROM python:3.10-alpine

WORKDIR /ticket

COPY ./ticket_service /ticket
COPY ../config.yaml /ticket
COPY ../requirements.txt /ticket

RUN pip3.10 install -r requirements.txt

EXPOSE 8070

CMD ["python3", "app/main.py"]
