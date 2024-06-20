# Use an official Python runtime as a parent image
FROM python:3.11.7-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Dask and Dask-Gateway
RUN pip install --no-cache-dir dask[complete] dask-gateway

COPY client.py .
COPY client2.py .

# Command to keep the container running
CMD ["tail", "-f", "/dev/null"]