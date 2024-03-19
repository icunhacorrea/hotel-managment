from python:3.11.8-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/hotel_managment

COPY ./requirements.txt .

RUN pip install -r requirements.txt
