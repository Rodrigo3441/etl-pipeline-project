"""
=====================================================
Load Data into Bronze Layer
=====================================================
Script Purpose:
    This script loads the extracted source data into the tables of the
    'bronze' schema. Before inserting new records, the existing data in each
    table is removed, ensuring the Bronze layer always contains a fresh copy
    of the source data.

Notes:
    - Uses pandas to load DataFrames into SQL Server.
    - Data is loaded within a single database transaction.
    - Existing rows are deleted before new data is inserted.
    - Table names are obtained dynamically from the extracted data dictionary.
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