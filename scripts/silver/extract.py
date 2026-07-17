"""
=====================================================
Extract Data from Bronze or Silver Layer
=====================================================
Script Purpose:
    This script extracts all data from the tables stored in the 'bronze' or 'silver'
    schema and loads each table into a pandas DataFrame. The extracted
    DataFrames are returned as a dictionary, where each key represents a
    table name and each value contains the corresponding DataFrame.

Notes:
    - Uses SQLAlchemy to connect to the database.
    - Dynamically retrieves all table names from bronze or silver schema.
    - Converts each query result into a pandas DataFrame.
    - Returns a dictionary containing the extracted Bronze tables,
      allowing subsequent transformation steps to process the data.
"""

from sqlalchemy import text
import pandas as pd

def return_all_tables_from_schema(engine, schema: str) -> list:

    # list containing all table names from specified layer
    tables = []

    with engine.connect() as conn:
        # retrieve all the table names from the specified schema
        result = conn.execute(text(f"""SELECT table_name 
                                       FROM information_schema.tables 
                                       WHERE table_schema = \'{schema}\'
                                    """)).fetchall()
        result = list(result)
        
        tables = [row.table_name for row in result]
    
    return tables


def execute(engine, schema: str) -> dict:
    # store all table names from bronze layer
    tables = return_all_tables_from_schema(engine, schema)

    # data dictionary that contains:
    # key:table_name value:dataframe of that table
    data_dict = {}

    with engine.connect() as conn:

        # for each table inside the list of tables from bronze layer
        for table_name in tables:

            # retrieve all the data from the table of table in the database
            result = conn.execute(text(f'SELECT * FROM {schema}.{table_name}')).fetchall()

            # converts the data into a dataframe
            result = pd.DataFrame(result)

            # create a new key in the dictionary and assign the dataframe correspondent to that table
            data_dict[f'{table_name}'] = result
            
    return data_dict
