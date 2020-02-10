FROM python:3.7.6

MAINTAINER cyy

COPY . /Blog
WORKDIR /Blog

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple