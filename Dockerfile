FROM python:3.9.4-buster

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD uvicorn main:app --host ${HOST} --port ${PORT} --reload