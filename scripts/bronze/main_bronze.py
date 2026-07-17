"""
=====================================================
Main Bronze Pipeline
=====================================================
Script Purpose:
    This script orchestrates the complete execution of the Bronze layer in the
    ETL pipeline. It creates the Bronze schema (if necessary), creates the
    required tables, extracts data from the source files, and loads the data
    into the Bronze layer. It also measures and displays the total execution
    time of the pipeline.

Notes:
    - Executes the Bronze layer in the following order:
        1. Create schema
        2. Create tables
        3. Extract source data
        4. Load data into the Bronze layer
    - Uses a single database connection throughout the pipeline.
    - Reports the total execution time after completion.
"""

from scripts import create_schema
from scripts.bronze import define_tables
from scripts.bronze import extract
from scripts import load
from database import connection
import time

def execute():
    engine = connection.get_connection()

    print('LOADING THE BRONZE LAYER')

    start_time = time.perf_counter()

    create_schema.execute(engine, 'bronze')
    define_tables.execute(engine, 'bronze')
    raw_data = extract.execute()
    load.execute(engine, raw_data, 'bronze')

    end_time = time.perf_counter()

    print(f'Bronze layer execution time: {(end_time - start_time):.6f} seconds')