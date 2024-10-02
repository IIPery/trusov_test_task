FROM python:3.11-slim

RUN apt-get update && apt-get upgrade
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /opt/app
WORKDIR /opt/app

RUN pip install -r requirements.txt
CMD python main.py