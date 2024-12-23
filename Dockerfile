FROM python:3.12-alpine

WORKDIR /app

COPY . /app/

RUN python -m pip install -U pip
RUN pip install -r /app/requirements.txt
