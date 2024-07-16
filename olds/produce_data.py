import pandas as pd
import dask.dataframe as dd
from dask import delayed

# Create sample data
data = {
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Furniture'],
    'Product': ['Laptop', 'Chair', 'Smartphone', 'Table', 'Tablet', 'Sofa'],
    'Quantity': [10, 5, 15, 7, 20, 3],
    'Unit_Price': [1000, 150, 800, 250, 500, 700]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
input_file = 'data.csv'
df.to_csv(input_file, index=False)
