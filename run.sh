#!/bin/bash
docker rmi dask-demo:alputer
docker build -t dask-demo:alputer .
kind load docker-image dask-demo:alputer
kubectl delete job dask-demo-job
kubectl apply -f job.yaml