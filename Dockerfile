FROM python:3

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get -y install vim

COPY ./django-customizable-blog /app

WORKDIR /app

RUN pip install -r requirements.txt
