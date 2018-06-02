FROM anapsix/alpine-java:8_jdk
MAINTAINER Herminio Vazquez

RUN apk add --update python python-dev py-pip build-base && pip install virtualenv && rm -rf /var/cache/apk/*
RUN pip install --upgrade pip
RUN pip install python-bioformats