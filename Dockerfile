FROM python:3

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get -y install vim

COPY ./workshop2020 /app

WORKDIR /app

