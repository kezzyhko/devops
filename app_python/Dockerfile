# syntax=docker/dockerfile:1

FROM python:3.9-alpine

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY ./app_files /app
WORKDIR /app
EXPOSE 5000
CMD python3 main.py
