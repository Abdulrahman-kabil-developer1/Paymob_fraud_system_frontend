FROM python:3.8-slim-buster

WORKDIR /front

COPY requirements.txt /front/
RUN pip install -r requirements.txt

COPY . /front/

 
#env variables 