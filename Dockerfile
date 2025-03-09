FROM --platform=linux/amd64 python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev

ADD requirements.txt /src/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY src/ /src/

