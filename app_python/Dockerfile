# syntax=docker/dockerfile:1

FROM python:3.9-alpine

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

EXPOSE 5000
CMD ["python3", "main.py"]

WORKDIR /app
COPY . /app
