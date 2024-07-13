# 1) Authenticate agains dask gateway
# 2) Get a personal cluster
# 3) Ask for a worker node
# 4) Submit the analysis


from dask_gateway import Gateway
from dask_gateway.auth import BasicAuth

gateway = Gateway(
    address="http://194.12.178.4:30081",
    auth=BasicAuth(username="alputer", password="dummy"),
)
gateway.list_clusters()

cluster = gateway.new_cluster()
cluster.scale(1)

client = cluster.get_client()

import dask.array as da

a = da.random.normal(size=(1000, 1000), chunks=(500, 500))

a.mean().compute()
