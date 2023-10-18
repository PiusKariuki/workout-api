FROM python:3.8-slim-buster

MAINTAINER PiusKariuki

WORKDIR /

COPY . .

COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]