FROM apache/airflow:2.6.1
USER root
RUN apt-get update && apt-get install -y \
	python3-dev \
	python3-pip
COPY requirements.txt /opt/requirements.txt
USER airflow
RUN pip install -r /opt/requirements.txt
