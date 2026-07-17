"""
=====================================================
Build Sales Fact
=====================================================
Script Purpose:
    This script builds the Sales Fact (`fact_sales`) for the Gold layer
    by combining sales transaction data with the Customer and Product
    dimensions. The resulting DataFrame is optimized for analytical
    queries and reporting.

Notes:
    - Removes technical Data Warehouse columns.
    - Joins sales transactions with the Product and Customer dimensions.
    - Replaces business identifiers with surrogate keys.
    - Selects only the columns required for analysis.
    - Renames columns using business-friendly names.
"""

import pandas as pd

def execute(
        crm_sales_details: pd.DataFrame, 
        dim_customers: pd.DataFrame, 
        dim_products: pd.DataFrame
    ) -> dict:

    # remove the data warehouse column information 
    crm_sales_details = crm_sales_details.drop('dwh_create_date', axis=1)

    # merge the sales details dataframe with others two dataframes that provides more information
    result = pd.merge(crm_sales_details, dim_products, how='left', left_on='sls_prd_key', right_on='product_number')
    result = pd.merge(result, dim_customers, how='left', left_on='sls_cust_id', right_on='customer_id')

    # select only the wanted columns
    result = result[
        [
            'sls_ord_num',
            'product_key',
            'customer_key',
            'sls_order_dt',
            'sls_ship_dt',
            'sls_due_dt',
            'sls_sales',
            'sls_quantity',
            'sls_price'
        ]
    ]

    # renaming columns for meaningful names
    result = result.rename(
        columns={
            'sls_ord_num': 'order_number',
            'sls_order_dt': 'order_date',
            'sls_ship_dt': 'shipping_date',
            'sls_due_dt': 'due_date',
            'sls_sales': 'sales_amount',
            'sls_quantity': 'quantity',
            'sls_price': 'price'
        }
    )

    return result