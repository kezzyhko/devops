# syntax=docker/dockerfile:1

FROM python:3.9-alpine

COPY ./requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt

WORKDIR /app
RUN adduser -D user && chown -R user /app
USER user
COPY ./app_files /app

EXPOSE 5000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:5000"]
