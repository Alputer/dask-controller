#from dask_kubernetes.operator import KubeCluster
import dask.delayed
from dask import compute
import dask.dataframe as dd
from dask.distributed import Client
import dask
import dask.array
import dask.delayed
import numpy as np
import pandas as pd
import os

# Code given below will be the image

DASK_SCHEDULER_URI = os.getenv("DASK_SCHEDULER_URI", "tcp://127.0.0.1:8080")

client = dask.distributed.Client(DASK_SCHEDULER_URI)

# Step 1: Create a delayed function to read the CSV file
@dask.delayed
def read_csv_delayed(file_path):
    return pd.read_csv(file_path)


@dask.delayed
def process_data(df):
    # Example transformation: Calculate total sales per category
    df['Total_Sales'] = df['Quantity'] * df['Unit_Price']
    
    # Example aggregation: Sum total sales by category
    result = df.groupby('Category').agg({'Total_Sales': 'sum'}).reset_index()
    
    return result

@dask.delayed
def write_csv_delayed(df, file_path):
    df.to_csv(file_path, index=False)
    print(f"Processed data written to {file_path}")


# Sample CSV file path
input_file = 'data.csv'
output_file = './output/output.csv'

# Create delayed tasks
delayed_df = read_csv_delayed(input_file)
delayed_processed = process_data(delayed_df)
delayed_write = write_csv_delayed(delayed_processed, output_file)

compute(delayed_write)
