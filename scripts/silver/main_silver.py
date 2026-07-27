"""
=====================================================
Silver Layer Pipeline
=====================================================
Script Purpose:
    This script orchestrates the execution of the Silver layer pipeline.
    It creates the Silver schema and tables (if they do not already exist),
    extracts data from the Bronze layer, applies all data transformations,
    and loads the cleaned and standardized data into the Silver layer.

Pipeline Flow:
    1. Connect to the database.
    2. Create the Silver schema.
    3. Create the Silver tables.
    4. Extract data from the Bronze layer.
    5. Apply table-specific transformations.
    6. Load the transformed data into the Silver layer.
"""

from database import connection
from scripts import create_schema
from scripts.silver import define_tables
from scripts.silver import extract
from scripts.silver import transform
from scripts import load
import time
import logging

logger = logging.getLogger()

def execute():  

    try:
        start_time = time.perf_counter()

        engine = connection.get_connection()
        
        logger.info('Creating Silver Schema')
        create_schema.execute(engine, 'silver')
        logger.info('Creating Silver Tables')
        define_tables.execute(engine, 'silver')
        logger.info('Extracting the Bronze Data')
        bronze_data = extract.execute(engine, 'bronze')
        logger.info('Transforming the Bronze Data')
        silver_data = transform.execute(bronze_data)
        logger.info('Loading the Bronze Data into Silver layer')
        load.execute(engine, silver_data, 'silver')

        end_time = time.perf_counter()

        total_time = end_time - start_time

        logger.info('Silver layer completed successfully')
        logger.info(f'Silver layer execution time: {(total_time):.6f} seconds')

        return total_time
    
    except Exception as e:
        logger.error('An error occurred while executing the silver layer')
        raise