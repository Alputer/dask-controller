#from dask_kubernetes.operator import KubeCluster
from dask.distributed import Client
import dask
import dask.array
import dask.delayed
import numpy as np
import os

# Code given below will be the image

DASK_SCHEDULER_URI = os.getenv("DASK_SCHEDULER_URI", "tcp://127.0.0.1:8080")
print(DASK_SCHEDULER_URI)

client = dask.distributed.Client(DASK_SCHEDULER_URI)

@dask.delayed
def load_data(filename):
    return np.load(filename)

@dask.delayed
def save_result(data, filename):
    np.savetxt(filename, data)
    return filename

# Load data using a Dask worker
data = load_data('data.npy')

# Convert to Dask array
x = dask.array.from_delayed(data, dtype=np.float64, shape=(10000, 10000))

# Perform computations
y = x + x.T
z = y[::2, 5000:].mean(axis=1)

# Compute the result
result = z.compute()

# Save the result using a Dask worker
output_filename = save_result(result, './output.txt')
output_filename.compute()
