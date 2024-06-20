from dask_gateway import Gateway
from dask_gateway.auth import BasicAuth

gateway = Gateway(
    address="http://194.12.178.4:30081",
    auth=BasicAuth(username="alputer", password="dummy"),
)

options = gateway.cluster_options()

cluster = gateway.new_cluster(
    worker_cores=0.4,
    worker_memory=0.3,
)  # config2.yaml
# cluster = gateway.new_cluster()  # config.yaml

cluster.scale(10)

print(options)
print(cluster)

client = cluster.get_client()

print(gateway.list_clusters())
print("##########")
print(cluster)
print("##########")
print(gateway.cluster_options())
print("##########")
print(client)

import dask.array as da

a = da.random.normal(size=(1000, 1000), chunks=(500, 500))

a.mean().compute()
