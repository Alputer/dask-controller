#Not Working
"""
from dask_kubernetes.operator import KubeCluster

cluster = KubeCluster(
    name="my-dask-cluster",
    image="ghcr.io/dask/dask:2024.1.0",
    shutdown_on_close=False
)
cluster.scale(3)

"""

from dask_kubernetes.operator import KubeCluster
from dask.distributed import Client
import dask
import dask.array



#cluster = KubeCluster(name="my-dask-cluster")
cluster = KubeCluster(
    name="my-dask-cluster",
    image="ghcr.io/dask/dask:2024.6.2",
    shutdown_on_close=True
)
cluster.scale(3)
client = Client(cluster)

x = dask.array.random.random((10000, 10000), chunks=(1000, 1000))
y = x + x.T
z = y[::2, 5000:].mean(axis=1)

result = z.compute()
print(result)

cluster.close()


# WORKING EXAMPLE
"""
from dask_kubernetes.operator import KubeCluster

cluster = KubeCluster(
    name="my-dask-cluster",
    image="ghcr.io/dask/dask:2024.1.0",
    shutdown_on_close=False
)
cluster.scale(1)
"""
"""
from dask_kubernetes.operator import KubeCluster

cluster = KubeCluster(
    name="mycluster",
    image="ghcr.io/dask/dask:latest",
    n_workers=3,
    env={"FOO": "bar"},
    resources={"requests": {"memory": "0.1Gi"}, "limits": {"memory": "0.2Gi"}},
)
"""
#from dask_kubernetes.operator import KubeCluster

#cluster = KubeCluster(name="my-dask-cluster", n_workers=3, image='ghcr.io/dask/dask:latest', resources={"requests": {"memory": "0.1Gi"}, "limits": {"memory": "0.2Gi"}})
