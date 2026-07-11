"""
=====================================================
Create Bronze Tables
=====================================================
Script Purpose:
    This script creates all required tables in the 'bronze' schema used by the
    Medallion Architecture. Before creating each table, it checks whether the
    table already exists to prevent duplicate creation.

    Table definitions are stored as DDL strings in a dictionary, allowing the
    creation process to be performed dynamically through a single reusable
    function.

Notes:
    - Uses SQLAlchemy to connect to the database.
    - Each table is created within its own transaction.
    - Existing tables are skipped without modification.
    - Any errors during table creation are reported without stopping the script.
"""

from sqlalchemy import text

cust_info_ddl = """
            cst_id             INT,
            cst_key			   NVARCHAR(50),
            cst_firstname	   NVARCHAR(50),
            cst_lastname	   NVARCHAR(50),
            cst_marital_status NVARCHAR(50),
            cst_gndr		   NVARCHAR(50),
            cst_create_date    DATE
"""

prd_info_ddl = """
            prd_id       INT,
            prd_key      NVARCHAR(50),
            prd_nm		 NVARCHAR(50),
            prd_cost	 INT,
            prd_line     NVARCHAR(50),
            prd_start_dt DATETIME,
            prd_end_dt   DATETIME
"""

sales_details_ddl = """
            sls_ord_num  NVARCHAR(50),
            sls_prd_key  NVARCHAR(50),
            sls_cust_id  INT,
            sls_order_dt INT,
            sls_ship_dt  INT,
            sls_due_dt   INT,
            sls_sales    INT,
            sls_quantity INT,
            sls_price    INT
"""

cust_az12_ddl = """
            cid   NVARCHAR(50),
            bdate DATE,
            gen   NVARCHAR(50)
"""

loc_a101_ddl = """
            cid   NVARCHAR(50),
	        cntry NVARCHAR(50)
"""

px_cat_g1v2_ddl = """
            id			NVARCHAR(50),
            cat			NVARCHAR(50),
            subcat		NVARCHAR(50),
            maintenance NVARCHAR(50)
"""

# # table names
# cust_info = 'crm_cust_info'
# prd_info = 'crm_prd_info'
# sales_details = 'crm_sales_details'

# cust_az12 = 'erp_cust_az12'
# loc_a101 = 'erp_loc_a101'
# px_cat_g1v2 = 'erp_px_cat_g1v2'

tables = {
    'crm_cust_info': cust_info_ddl,
    'crm_prd_info': prd_info_ddl,
    'crm_sales_details': sales_details_ddl,
    'erp_cust_az12': cust_az12_ddl,
    'erp_loc_a101': loc_a101_ddl,
    'erp_px_cat_g1v2': px_cat_g1v2_ddl
}


def create_table(engine, table_name, ddl, schema):
    
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


def execute(engine):
    for table_name, ddl in tables.items():
        create_table(engine, table_name, tables[table_name], 'bronze')


