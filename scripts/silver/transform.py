"""
=====================================================
Transform Silver Layer Data
=====================================================
Script Purpose:
    This script orchestrates the transformation process for the Silver
    layer. It determines which transformation function should be applied
    to each Bronze table and executes the corresponding business rules.

Notes:
    - Receives the extracted Bronze data as a dictionary of DataFrames.
    - Delegates the transformation logic to the appropriate module for
      each table.
    - Returns a dictionary containing the transformed DataFrames, ready
      to be loaded into the Silver layer.
"""

from scripts.silver.transformations.crm_cust_info import execute as transform_crm_cust_info
from scripts.silver.transformations.crm_prd_info import execute as transform_crm_prd_info
from scripts.silver.transformations.crm_sales_details import execute as transform_crm_sales_details
from scripts.silver.transformations.erp_cust_az12 import execute as transform_erp_cust_az12
from scripts.silver.transformations.erp_loc_a101 import execute as transform_erp_loc_a101
from scripts.silver.transformations.erp_px_cat_g1v2 import execute as transform_erp_px_cat_g1v2

import pandas as pd

def run_table_transformation(table_name: str, df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies the appropriate transformation rules based on the table name.
    """

    print(f'Transforming {table_name} table')

    match table_name:
        case 'crm_cust_info':
            return transform_crm_cust_info(df)
        
        case 'crm_prd_info':
            return transform_crm_prd_info(df)

        case 'crm_sales_details':
            return transform_crm_sales_details(df)

        case 'erp_cust_az12':
            return transform_erp_cust_az12(df)
        
        case 'erp_loc_a101':
            return transform_erp_loc_a101(df)
        
        case 'erp_px_cat_g1v2':
            return transform_erp_px_cat_g1v2(df)


def execute(data: dict) -> dict:
    """
    Iterates through all extracted Bronze tables, applies the corresponding
    transformation to each DataFrame, and returns the transformed data.
    """

    for table_name, df in data.items():
    
        df = run_table_transformation(table_name, df)
        data.update({table_name: df})

    return data

