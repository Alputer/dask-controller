from dask_gateway import Gateway
from dask_gateway.auth import BasicAuth

gateway = Gateway(
    address="http://192.168.1.40:30081",
    auth=BasicAuth(username="alputer", password="dummy"),
)
gateway.list_clusters()

# cluster = gateway.new_cluster()
# cluster = gateway.new_cluster(worker_cores=1, worker_memory=1) # Does not create worker pod --> Silence error?
cluster = gateway.new_cluster()
# cluster.scale(2)
cluster.adapt(2, 6)  # Similar to cluster.scale but this is dynamic

client = cluster.get_client()
print(client)

import dask.array as da

a = da.random.normal(size=(1000, 1000), chunks=(500, 500))

a.mean().compute()
