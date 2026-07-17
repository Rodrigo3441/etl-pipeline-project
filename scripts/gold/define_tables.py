"""
=====================================================
Define Gold Layer Tables
=====================================================
Script Purpose:
    This script defines the table structures for the Gold layer and
    creates them in the database if they do not already exist.

    The Gold layer contains the business-ready dimensional model,
    including the Customer Dimension, Product Dimension, and Sales
    Fact table used for reporting and analytics.

Notes:
    - Defines the schema for all Gold tables.
    - Uses the shared table creation utility.
    - Creates only tables that do not already exist.
"""

from scripts import create_table

dim_customers_ddl = """
        customer_key INT,
        customer_id INT,
        customer_number NVARCHAR(50),
        first_name NVARCHAR(50),
        last_name NVARCHAR(50),
        country NVARCHAR(50),
        marital_status NVARCHAR(50),
        gender NVARCHAR(50),
        birthdate DATE,
        create_date DATE
""" 

dim_products_ddl = """
        product_key INT,
        product_id INT,
        product_number NVARCHAR(50),
        product_name NVARCHAR(50),
        category_id NVARCHAR(50),
        category NVARCHAR(50),
        subcategory NVARCHAR(50),
        maintenance NVARCHAR(50),
        product_cost INT,
        product_line NVARCHAR(50),
        product_start_date DATE
"""

fact_sales_ddl = """
        order_number NVARCHAR(50),
        product_key INT,
        customer_key INT,
        order_date DATE,
        shipping_date DATE,
        due_date DATE,
        sales_amount INT,
        quantity INT,
        price INT
"""

tables = {
    'dim_customers': dim_customers_ddl,
    'dim_products': dim_products_ddl,
    'fact_sales': fact_sales_ddl
}

def execute(engine, schema):
    for table_name, ddl in tables.items():
        create_table.execute(engine, table_name, ddl, schema)


