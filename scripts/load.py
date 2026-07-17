"""
=====================================================
Load Data into Data Warehouse Layer
=====================================================
Script Purpose:
    This script loads pandas DataFrames into the specified data warehouse
    layer (Bronze, Silver, or Gold). Before inserting new records, the
    existing data in each table is removed, ensuring the target layer
    always contains the latest version of the processed data.

Notes:
    - Uses pandas to load DataFrames into SQL Server.
    - Executes all insert operations within a single database transaction.
    - Existing rows are removed before new data is inserted.
    - The target schema is provided dynamically.
    - Table names are obtained from the input data dictionary.
"""

import pandas as pd

def execute(engine, data, schema):
    # transaction is started to insert the data into the bronze layer
    # insertion date format: truncate and insert
    with engine.begin() as conn:
        for table_name, df in data.items():
    
            df.to_sql(
                        name=table_name, 
                        con=conn, 
                        schema=schema,
                        if_exists='delete_rows', 
                        index=False
                     )