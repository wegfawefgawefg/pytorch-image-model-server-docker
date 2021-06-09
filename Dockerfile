FROM ubuntu:20.04
# FROM python:3.8
# FROM nvidia/cuda-arm64:11.3.1-base-ubuntu20.04

LABEL maintainer="Gibson Martin" \
    email="gibson@cratustech.com"

RUN apt-get update
RUN apt-get install --no-install-recommends -y python3.8 python3-pip
# RUN apt-get install --no-install-recommends -y python3.8 python3-pip python3.8-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

EXPOSE 8080 8080

ENTRYPOINT [ "python3" ]

CMD [ "/app/app.py" ]
