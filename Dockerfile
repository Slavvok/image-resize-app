FROM python:3.6
ENV PYTHONBUFFERED 1

RUN mkdir -p /app/code
WORKDIR /app/code
ADD requirements.txt /app/code/

RUN pip3 install --upgrade pip && pip3 install --upgrade pip-tools && pip-sync requirements.txt

COPY . /app/code
