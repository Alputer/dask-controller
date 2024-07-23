#!/bin/bash
# One time only --> helm install --repo https://helm.dask.org --create-namespace -n dask-operator --generate-name dask-kubernetes-operator
docker rmi dask-demo:alputer
docker build -t dask-demo:alputer .
kind load docker-image dask-demo:alputer
kubectl delete -f job.yaml # This also deletes the autoscaler.
kubectl delete -f cluster.yaml # This also deletes the autoscaler.
kubectl delete -f autoscaler.yaml # This also deletes the autoscaler.
sleep 1
kubectl apply -f autoscaler.yaml
sleep 1
kubectl apply -f cluster.yaml
sleep 1

DASK_SCHEDULER_URI=$(kubectl get services simple-scheduler | awk 'NR==2 {print "tcp://" $3 ":" substr($5,0,4)}')
export DASK_SCHEDULER_URI
envsubst < job.yaml | kubectl apply -f -

#kubectl apply -f job.yaml
# check http://localhost:30008
