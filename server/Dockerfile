FROM python:3.10-slim-buster

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app

ADD . .

CMD [ "python3","app.py" ]