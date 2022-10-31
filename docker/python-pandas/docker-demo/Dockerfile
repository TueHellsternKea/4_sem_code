# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install pandas
COPY . .
CMD [ "python", "demo1_app.py"]