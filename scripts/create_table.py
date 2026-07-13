"""
=====================================================
Create Database Table
=====================================================
Script Purpose:
    This script checks whether a specified table already exists within a
    database schema. If the table is not found, it is created using the
    provided Data Definition Language (DDL). If the table already exists,
    the creation process is skipped.

Notes:
    - Uses SQLAlchemy to connect to the database.
    - Accepts the schema name, table name, and DDL definition as parameters,
      allowing it to be reused across different layers of the pipeline.
    - The table creation is executed within a transaction to ensure
      consistency.
    - Existing tables are skipped without modification.
    - Any errors during table creation are reported to the user.
"""
from sqlalchemy import text

def execute(engine, table_name, ddl, schema):
    
    # a simple query is executed to find out if the table already exists
    with engine.connect() as conn:
        table_exists = conn.execute(
            text(f"""SELECT 1 FROM information_schema.tables 
                     WHERE table_schema = \'{schema}\' 
                     AND table_name = \'{table_name}\'""")
        ).fetchone()

    # if the table doesn't exists, the script will create it
    if table_exists is None:
        
        print(f'Table {table_name} not found, creating the table')

        try:
            # a transaction is started and the table created
            with engine.begin() as conn:
                conn.execute(text(f"""CREATE TABLE {schema}.{table_name} 
                                                        ( {ddl} )
                                                        """))

            print(f'Table {table_name} created successfully')

        except Exception as e:
            print(f'An error occurred while trying to create the table {table_name}: {e}')

    else:
        print(f'Table {table_name} has been found, skipping its creation')