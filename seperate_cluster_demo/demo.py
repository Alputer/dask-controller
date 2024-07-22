#from dask_kubernetes.operator import KubeCluster
import dask.delayed
from dask import compute
import dask.dataframe as dd
from dask.distributed import Client
import dask
import dask.array
import dask.delayed
import pandas as pd
import time


from dask.distributed import Client

client = Client()


@dask.delayed
def read_csv_delayed(file_path):
    import wikipedia
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
    time.sleep(20)
    df.to_csv(file_path, index=False)
    print(f"Processed data written to {file_path}")


# Sample CSV file path
input_file = './app/output/data.csv'
output_file = './app/output/output.csv'

# Create delayed tasks
delayed_df = read_csv_delayed(input_file)
delayed_processed = process_data(delayed_df)
delayed_write = write_csv_delayed(delayed_processed, output_file)

compute(delayed_write)
