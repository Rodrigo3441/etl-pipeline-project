"""
=====================================================
Extract Source Data
=====================================================
Script Purpose:
    This script extracts data from the CRM and ERP source CSV files and loads
    them into pandas DataFrames. The extracted data is returned as a dictionary,
    where each key represents a table name and each value contains the
    corresponding DataFrame.

Notes:
    - Uses pandas to read CSV files.
    - Data is extracted from both CRM and ERP source directories.
    - If an error occurs during extraction, it is reported to the user.
"""

import pandas as pd

def execute():
    try: 
        return {
        'crm_cust_info': pd.read_csv('datasets/source_crm/cust_info.csv'),
        'crm_prd_info': pd.read_csv('datasets/source_crm/prd_info.csv'),
        'crm_sales_details': pd.read_csv('datasets/source_crm/sales_details.csv'),
        'erp_cust_az12': pd.read_csv('datasets/source_erp/cust_az12.csv'),
        'erp_loc_a101': pd.read_csv('datasets/source_erp/loc_a101.csv'),
        'erp_px_cat_g1v2': pd.read_csv('datasets/source_erp/px_cat_g1v2.csv')
        }
    except Exception as e:
        print(f'An error occurred while trying to extract the data: {e}')
    