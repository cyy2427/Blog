FROM python:3.7.5

MAINTAINER chenyuyi@zkyouxi.com

COPY . /helloflask
WORKDIR /helloflask

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && flask db init \
    && flask db migrate \
    && flask db upgrade

EXPOSE 6666

CMD ["gunicorn", "app:app", "-c", "./gunicorn.py"]