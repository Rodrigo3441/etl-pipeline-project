"""
=====================================================
Create Bronze Layer Tables
=====================================================
Script Purpose:
    This script defines the table structures for the Bronze layer and
    creates each table by invoking the reusable table creation function.
    Each table is created only if it does not already exist in the
    'bronze' schema.

Notes:
    - Stores the Data Definition Language (DDL) for each Bronze table.
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

tables = {
    'crm_cust_info': cust_info_ddl,
    'crm_prd_info': prd_info_ddl,
    'crm_sales_details': sales_details_ddl,
    'erp_cust_az12': cust_az12_ddl,
    'erp_loc_a101': loc_a101_ddl,
    'erp_px_cat_g1v2': px_cat_g1v2_ddl
}

def execute(engine):
    for table_name, ddl in tables.items():
        create_table.execute(engine, table_name, tables[table_name], 'bronze')


