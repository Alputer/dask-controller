#from dask_kubernetes.operator import KubeCluster
from dask.distributed import Client
import dask
import dask.array
import numpy as np
import os

"""
cluster = KubeCluster(
    name="my-dask-cluster",
    image="ghcr.io/dask/dask:2024.1.0",
    shutdown_on_close=True
)
cluster.adapt(minimum=1, maximum=10)
client = Client(cluster)
"""



# Code given below will be the image

DASK_SCHEDULER_URI = os.getenv("DASK_SCHEDULER_URI", "tcp://127.0.0.1:8080")
print(DASK_SCHEDULER_URI)
print('hey1')
client = dask.distributed.Client(DASK_SCHEDULER_URI)

x = dask.array.random.random((10000, 10000), chunks=(1000, 1000))
y = x + x.T
z = y[::2, 5000:].mean(axis=1)

data = np.load('data.npy')
x = dask.array.from_array(data, chunks=(1000, 1000))

result = z.compute()

np.savetxt('./output/output.txt', result)
with open("./output/hello.txt", "w") as my_file:
    my_file.write("Hello world \n")
print("hey2")