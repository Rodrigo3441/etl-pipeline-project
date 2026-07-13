from database import connection
from scripts import create_schema
from scripts.silver import define_tables
from scripts.silver import extract
from scripts.silver import transform
from scripts.bronze import load
import time

def execute():  
    engine = connection.get_connection()

    print('LOADING THE SILVER LAYER')
    
    create_schema.execute(engine, 'silver')
    define_tables.execute(engine)

    data = extract.execute(engine)
    data_transformed = transform.execute(data)

    load.execute(engine, data_transformed, 'silver')