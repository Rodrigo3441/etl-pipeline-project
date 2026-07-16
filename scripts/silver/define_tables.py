"""
=====================================================
Create Silver Layer Tables
=====================================================
Script Purpose:
    This script defines the table structures for the Silver layer and
    creates each table by invoking the reusable table creation function.

Notes:
    - Stores the Data Definition Language (DDL) for each Silver table.
    - Uses a dictionary to associate table names with their DDL definitions.
    - Iterates through all table definitions and delegates the creation
      process to the reusable table creation script.
    - Existing tables are skipped without modification.
"""

from scripts import create_table

cust_info_ddl = """
cst_id INT,
cst_key NVARCHAR(50),
cst_firstname NVARCHAR(50),
cst_lastname NVARCHAR(50),
cst_marital_status NVARCHAR(50),
cst_gndr NVARCHAR(50),
cst_create_date DATE,
dwh_create_date DATETIME2 DEFAULT GETDATE()
"""

prd_info_ddl = """
prd_id INT,
cat_id NVARCHAR(50),
prd_key NVARCHAR(50),
prd_nm NVARCHAR(50),
prd_cost INT,
prd_line NVARCHAR(50),
prd_start_dt DATE,
prd_end_dt DATE,
dwh_create_date DATETIME2 DEFAULT GETDATE()
"""

prd_sales_details_ddl = """
sls_ord_num NVARCHAR(50),
sls_prd_key NVARCHAR(50),
sls_cust_id INT,
sls_order_dt DATE,
sls_ship_dt DATE,
sls_due_dt DATE,
sls_sales INT,
sls_quantity INT,
sls_price INT,
dwh_create_date DATETIME2 DEFAULT GETDATE()
"""

cust_az12_ddl = """
cid NVARCHAR(50),
bdate DATE,
gen NVARCHAR(50),
dwh_create_date DATETIME2 DEFAULT GETDATE()
"""

loc_a101_dll = """
cid NVARCHAR(50),
cntry NVARCHAR(50),
dwh_create_date DATETIME2 DEFAULT GETDATE()
"""

px_cat_g1v2_dll = """
id NVARCHAR(50),
cat	NVARCHAR(50),
subcat NVARCHAR(50),
maintenance NVARCHAR(50),
"""

tables = {
    'crm_cust_info': cust_info_ddl,
    'crm_prd_info': prd_info_ddl,
    'crm_sales_details': prd_sales_details_ddl,
    'erp_cust_az12': cust_az12_ddl,
    'erp_loc_a101': loc_a101_dll,
    'erp_px_cat_g1v2': px_cat_g1v2_dll
}

def execute(engine):
    for table_name, ddl in tables.items():
        create_table.execute(engine, table_name, ddl, 'silver')

