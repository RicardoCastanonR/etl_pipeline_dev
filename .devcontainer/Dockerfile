FROM alpine:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apk update

RUN apk add openjdk17
RUN apk add python3 py3-pip
RUN apk add wget
RUN apk add bash

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk

# =================== #
# PYTHON DEPENDENCIES #
# =================== #
WORKDIR /workspace


#RUN pip3 install pyspark
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
# COPY requirements.txt .
# RUN pip3 install --no-cache-dir -r requirements.txt || true
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir pyspark pandas


ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

# ENV HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"