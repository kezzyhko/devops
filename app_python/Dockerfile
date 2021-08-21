# syntax=docker/dockerfile:1

FROM ubuntu:20.04

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY ./app_files /app
WORKDIR /app
EXPOSE 5000
CMD python3 main.py
