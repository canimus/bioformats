FROM python:3.7.2
MAINTAINER Herminio Vazquez

RUN apt-get update
RUN apt-get install -y python3-openslide
RUN apt-get install -y openjdk-8-jdk
RUN pip install openslide-python
RUN pip install python-bioformats
RUN pip install PyFunctional
RUN pip install pychalk
RUN pip install matplotlib
RUN pip install networkx
RUN pip install scikit-learn
RUN pip install statsmodels
RUN pip install lxml
