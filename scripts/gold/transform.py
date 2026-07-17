"""
=====================================================
Gold Layer Transformation Orchestrator
=====================================================
Script Purpose:
    This script orchestrates the transformation process for the Gold layer.
    It builds the business-ready dimensions and fact table by executing the
    corresponding transformation modules and collecting their outputs into
    a single dictionary for the loading step.

Pipeline Flow:
    1. Build the Customer Dimension.
    2. Build the Product Dimension.
    3. Build the Sales Fact table using the generated dimensions.
    4. Collect all Gold tables into a dictionary.
    5. Return the transformed data for loading into the Gold layer.
"""

from scripts.gold.transformations import dim_customers
from scripts.gold.transformations import dim_products
from scripts.gold.transformations import fact_sales

import pandas as pd

def execute(data: dict) -> dict:

    # execute and stores data transformations for dimensions customers
    dim_customers_data = dim_customers.execute(
            data['crm_cust_info'], 
            data['erp_cust_az12'], 
            data['erp_loc_a101']
        )

    # execute and stores data transformations for dimensions products
    dim_products_data = dim_products.execute(
            data['crm_prd_info'],
            data['erp_px_cat_g1v2']
        )

    # execute and stores data transformations for fact sales
    fact_sales_data = fact_sales.execute(
            data['crm_sales_details'],
            dim_customers_data,
            dim_products_data
        )
    
    # update data to an empty dictionary
    data = {}

    # append new transformed data into the data dictionary
    data['dim_customers'] = dim_customers_data
    data['dim_products'] = dim_products_data
    data['fact_sales'] = fact_sales_data

    return data

    
        
