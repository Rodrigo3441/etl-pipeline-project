# import pyodbc as db
from sqlalchemy import create_engine

# database credentials
server = 'localhost\\SQLEXPRESS'
database = 'DataEngineeringLearning'
driver = 'ODBC Driver 17 for SQL Server'

# def get_connection_pyodbc():
#     try:
#         conn = db.connect(
#             f'DRIVER={driver};'
#             f'SERVER={server};'
#             f'DATABASE={database};'
#             'Trusted_Connection=yes;'
#         )
#         conn.autocommit = True
#         return conn
    
#     except db.Error as e:
#         print("Error while connecting to database:", e)
#         return None


def get_connection():
    try:
        conn = create_engine(f'mssql://{server}/{database}?driver={driver}&trusted_connection=yes')
        return conn
    
    except Exception as e:
        print("Error while connecting to database by sqlalchemy:", e)
