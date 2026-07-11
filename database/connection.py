"""
=====================================================
Database Connection
=====================================================
Script Purpose:
    This script establishes a connection to the SQL Server database using
    SQLAlchemy. It defines the database connection settings and provides a
    reusable function that returns a database engine for use throughout the
    ETL pipeline.

Notes:
    - Uses Windows Authentication (Trusted Connection).
    - Creates a SQLAlchemy engine for SQL Server.
    - Database credentials are defined as configuration variables.
    - Reports an error if the connection cannot be established.
"""

from sqlalchemy import create_engine

# database credentials
server = 'localhost\\SQLEXPRESS'
database = 'DataEngineeringLearning'
driver = 'ODBC Driver 17 for SQL Server'

def get_connection():
    try:
        conn = create_engine(f'mssql://{server}/{database}?driver={driver}&trusted_connection=yes')
        return conn
    
    except Exception as e:
        print("Error while connecting to database by sqlalchemy:", e)
