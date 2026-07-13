"""
=====================================================
Create Silver Layer Tables
=====================================================
Script Purpose:
    This script defines the table structures for the Silver layer and
    creates each table by invoking the reusable table creation function.
    As the project evolves, additional Silver tables will be added to
    support the transformed data from the Bronze layer.

Notes:
    - Stores the Data Definition Language (DDL) for each Silver table.
    - Uses a dictionary to associate table names with their DDL definitions.
    - Iterates through all table definitions and delegates the creation
      process to the reusable table creation script.
    - Existing tables are skipped without modification.
"""

from scripts import create_table

cust_info_ddl = """
                cst_id             INT,
                cst_key			   NVARCHAR(50),
                cst_firstname	   NVARCHAR(50),
                cst_lastname	   NVARCHAR(50),
                cst_marital_status NVARCHAR(50),
                cst_gndr		   NVARCHAR(50),
                cst_create_date    DATE,
                dwh_create_date    DATETIME2 DEFAULT GETDATE()
"""

tables = {
    'crm_cust_info': cust_info_ddl
}

def execute(engine):
    for table_name, ddl in tables.items():
        create_table.execute(engine, table_name, tables[table_name], 'silver')

