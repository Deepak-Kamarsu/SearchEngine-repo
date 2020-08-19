FROM python:3.7.2-stretch

WORKDIR /app

ADD . /app

CMD ["python", "main.py"]