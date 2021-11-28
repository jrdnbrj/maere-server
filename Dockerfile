FROM python:3.9.4-buster

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT} --ssl-keyfile=${SSL_KEYFILE} --ssl-certfile=${SSL_CERTFILE}