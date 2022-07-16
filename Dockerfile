FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.prd.txt /app/requirements.prd.txt
RUN pip install -r requirements.prd.txt
COPY . /app