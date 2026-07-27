"""
=====================================================
Create Database Schema
=====================================================
Script Purpose:
    This script checks whether a specified database schema already exists.
    If the schema is not found, it creates it before the pipeline continues.
    If the schema already exists, the pipeline proceeds without making any
    changes.

Notes:
    - Uses SQLAlchemy to connect to the database.
    - Accepts the schema name as a parameter, allowing it to be reused
      for the Bronze, Silver, and Gold layers.
    - The schema creation is executed within a transaction to ensure
      consistency.
    - If an error occurs during schema creation, the pipeline is stopped.
"""
from sqlalchemy import text
import logging

logger = logging.getLogger()

def execute(engine, schema):

    # execute a simple query to find out the schema already exists
    with engine.connect() as conn:
        schema_exists = conn.execute(
            text(f"""SELECT 1 FROM information_schema.schemata 
                 WHERE schema_name = :schema
                 """),
            {"schema": schema}
        ).fetchone()


        # check if the specified schema already exists
        
        if schema_exists is None:
            logger.info(f'{schema} schema not found, creating it.')

            try:
                # create the specified schema in the database to store tables from the corresponding layer
                # a transaction is started
                with engine.begin() as conn:
                    conn.execute(text(f'CREATE SCHEMA {schema}'))

                logger.info(f'Schema \'{schema}\' created successfully')

            except Exception as e:
                logger.exception(f"Failed to create schema '{schema}'.")
                raise

        else:
            logger.info(f'Schema \'{schema}\' already exists.')