FROM ghcr.io/dask/dask:2024.1.0

WORKDIR /app

COPY data.csv /app/
COPY demo.py /app/