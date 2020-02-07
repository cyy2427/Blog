FROM python:3.7.6

MAINTAINER cyy

COPY . /helloflask
WORKDIR /helloflask

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple