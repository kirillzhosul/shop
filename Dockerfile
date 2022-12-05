# syntax=docker/dockerfile:1
FROM python:3.10.7-alpine

# Disable python buffering and bytecode *.pyc compiling. 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Project directory.
WORKDIR /srv/www/kirillzhosul/shop

# Install requirements.
COPY requirements.txt /srv/www/kirillzhosul/shop/
RUN apk add build-base
RUN pip install --upgrade pip
RUN pip install --upgrade --no-cache-dir -r requirements.txt

# Copy whole project.
COPY ./src/ /srv/www/kirillzhosul/shop/

# Run project.
CMD ["python run.py"]
