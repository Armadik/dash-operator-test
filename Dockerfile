# Build the manager binary
FROM python:3.8-alpine

ADD . /app

RUN pip3 install /app

ENTRYPOINT ["dashoper"]