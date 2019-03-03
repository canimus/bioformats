FROM python:3.7.2
MAINTAINER Herminio Vazquez

RUN apt-get update
RUN apt-get install -y python3-openslide
RUN apt-get install -y openjdk-8-jdk
RUN pip install --no-cache openslide-python
RUN pip install --no-cache python-bioformats
RUN pip install --no-cache PyFunctional
RUN pip install --no-cache pychalk
RUN pip install --no-cache matplotlib
RUN pip install --no-cache networkx
RUN pip install --no-cache scikit-learn
RUN pip install --no-cache statsmodels
RUN pip install --no-cache lxml
RUN pip install --no-cache pandas
RUN pip install --no-cache seaborn
RUN pip install --no-cache jupyterlab
RUN pip uninstall -y tornado
RUN pip install --no-cache tornado==5.1.1

EXPOSE 8000
ENTRYPOINT jupyter lab --allow-root --ip=0.0.0.0 --port=8000 --NotebookApp.token=''
