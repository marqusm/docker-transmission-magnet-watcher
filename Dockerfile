FROM python:3-alpine

MAINTAINER Marko Miskovic <marko.miskovic@gmx.com>

COPY app/ /
RUN \
  pip install -r /app/requirements.txt
  mkdir /log

ENTRYPOINT ["python3", "/app/script.py"]
