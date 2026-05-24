FROM python:3.10-alpine

WORKDIR /bonus

COPY ./bonus_service /bonus
COPY ../config.yaml /bonus
COPY ../requirements.txt /bonus

RUN pip3.10 install -r requirements.txt

EXPOSE 8050

CMD ["python3", "app/main.py"]
