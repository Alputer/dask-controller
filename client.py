from dask_gateway import Gateway

gateway = Gateway("http://194.12.178.4:30081")
gateway.list_clusters()

cluster = gateway.new_cluster()
cluster.scale(1)

client = cluster.get_client()

import dask.array as da

a = da.random.normal(size=(1000, 1000), chunks=(500, 500))

a.mean().compute()
