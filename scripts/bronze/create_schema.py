"""
=====================================================
Create Bronze Schema
=====================================================
Script Purpose:
    This function checks whether the 'bronze' schema already exists in the database.
    If the schema is not found, it creates it before the extraction process begins.
    If the schema already exists, the pipeline continues without making any changes.

Notes:
    - Uses SQLAlchemy to connect to the database.
    - The schema creation is executed within a transaction to ensure consistency.
    - If an error occurs during schema creation, the pipeline is stopped.
"""

from sqlalchemy import text

def execute(engine):

    # execute a simple query to find out the schema already exists
    with engine.connect() as conn:
        schema_exists = conn.execute(
            text("""SELECT 1 FROM information_schema.schemata 
                 WHERE schema_name = 'bronze'""")
        ).fetchone()


        # check if the bronze schema already exists
        
        if schema_exists is None:
            print('Bronze schema not found, creating the bronze schema:')

            try:
                # create the bronze schema in the database to store tables from bronze layer
                # a transaction is started
                with engine.begin() as conn:
                    conn.execute(text('CREATE SCHEMA bronze'))

                print('Bronze schema created successfully')

            except Exception as e:
                print(f'An error occurred while trying to create the bronze schema: {e}')
                print('Stopping the bronze pipeline')
                return

        else:
            print('Bronze schema has been found, continuing the extract process')