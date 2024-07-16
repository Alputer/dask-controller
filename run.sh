#!/bin/bash
# One time only --> helm install --repo https://helm.dask.org --create-namespace -n dask-operator --generate-name dask-kubernetes-operator
docker rmi dask-demo:alputer
docker build -t dask-demo:alputer .
kind load docker-image dask-demo:alputer
kubectl delete -f dask-job.yaml
kubectl delete -f autoscaler.yaml
sleep 3
kubectl apply -f autoscaler.yaml
kubectl apply -f dask-job.yaml
