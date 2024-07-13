# Use an official Python runtime as a parent image
FROM python:3.11.7-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Dask and Dask-Gateway

COPY client.py .
COPY client2.py .
COPY client3.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

# Command to keep the container running
CMD ["tail", "-f", "/dev/null"]