#!/bin/bash
helm delete dask
sleep 3
helm install dask dask/dask -f values.yaml --version 2024.1.1
sleep 3
docker rmi dask-demo:alputer
docker build -t dask-demo:alputer .
kind load docker-image dask-demo:alputer
kubectl delete job dask-demo-job
# For HostPath
DASK_SCHEDULER_URI=$(kubectl get services dask-scheduler | awk 'NR==2 {print "tcp://" $3 ":" substr($5,0,4)}')
export DASK_SCHEDULER_URI
envsubst < job.yaml | kubectl apply -f -
sleep 5
kubectl port-forward service/simple-job-scheduler 8787:8787