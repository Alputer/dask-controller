#!/bin/bash
docker rmi dask-demo:alputer
docker build -t dask-demo:alputer .
kind load docker-image dask-demo:alputer
kubectl delete job dask-demo-job
# For HostPath
kubectl apply -f job.yaml

# For persistent volume
#kubectl apply -f persistent_volume.yaml
#kubectl apply -f job2.yaml