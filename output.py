import numpy as np

# Create some data
data = np.random.random((10000, 10000))

# Save the data to a .npy file
np.save('data.npy', data)
