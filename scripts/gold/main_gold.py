"""
=====================================================
Gold Layer Pipeline
=====================================================
Script Purpose:
    This script orchestrates the execution of the Gold layer pipeline.
    It creates the Gold schema and tables (if they do not already exist),
    extracts data from the Silver layer, builds the business-ready
    dimensions and fact table, and loads the final analytical data into
    the Gold layer.

Pipeline Flow:
    1. Connect to the database.
    2. Create the Gold schema.
    3. Create the Gold tables.
    4. Extract data from the Silver layer.
    5. Build the dimensions and fact table.
    6. Load the transformed data into the Gold layer.
"""

from scripts import create_schema
from scripts.silver import extract
from scripts.gold import transform
from scripts import load
from scripts.gold import define_tables
from database import connection
import time

def execute():

    try:
        start_time = time.perf_counter()

        engine = connection.get_connection()

        print('LOADING THE GOLD LAYER')
        
        create_schema.execute(engine, 'gold')
        define_tables.execute(engine, 'gold')
        silver_data = extract.execute(engine, 'silver')
        gold_data = transform.execute(silver_data)
        load.execute(engine, gold_data, 'gold')

        end_time = time.perf_counter()

        total_time = end_time - start_time

        print(f'Gold layer execution time: {(total_time):.6f} seconds')

        return total_time
    
    except Exception as e:
        print('An error occurred while executing the gold layer')
        raise

    

