"""
=====================================================
Build Product Dimension
=====================================================
Script Purpose:
    This script builds the Product Dimension (`dim_products`) for the
    Gold layer by combining product information from multiple Silver
    tables into a single business-ready DataFrame.

Notes:
    - Removes technical Data Warehouse columns.
    - Merges product information with product category data.
    - Keeps only the current version of each product.
    - Removes unnecessary columns after the merge.
    - Creates a surrogate key for analytical purposes.
    - Renames and reorders columns to produce the final
      Product Dimension.
"""

import pandas as pd

def execute(
        crm_prd_info: pd.DataFrame, 
        erp_px_cat_g1v2: pd.DataFrame
    ) -> dict:

    # remove the data warehouse column information 
    crm_prd_info = crm_prd_info.drop('dwh_create_date', axis=1)
    erp_px_cat_g1v2 = erp_px_cat_g1v2.drop('dwh_create_date', axis=1)

    # merge the product info dataframe with category dataframe that provides more information
    result = pd.merge(crm_prd_info, erp_px_cat_g1v2, how='left', left_on='cat_id', right_on='id')

    # remove historical data from the products
    result = result.where(result['prd_end_dt'].isna())

    # remove lines that were removed by the previous step
    result = result.dropna(axis=0, how='all')

    # removed unused columns from the result
    result = result.drop('id', axis=1)
    result = result.drop('prd_end_dt', axis=1) # this column only contains NULLs

    # sort the data by the prd_start_dt and prd_key before creating a new primary key for data aggregations
    result = result.sort_values(by=['prd_start_dt', 'prd_key'])

    # create a primary key column for data aggregations
    result['product_key'] = range(1, len(result) + 1)

    # renaming columns for meaningful names
    result = result.rename(
        columns={
            'prd_id': 'product_id',
            'cat_id': 'category_id',
            'prd_key': 'product_number',
            'prd_nm': 'product_name',
            'prd_cost': 'product_cost',
            'prd_line': 'product_line',
            'prd_start_dt': 'product_start_date',
            'cat': 'category',
            'subcat': 'subcategory'
        }
    )

    # reorder columns to improve consistency
    result = result[
        [   
            'product_key',
            'product_id',
            'product_number',
            'product_name',
            'category_id',
            'category',
            'subcategory',
            'maintenance',
            'product_cost',
            'product_line',
            'product_start_date'
        ]
    ]

    return result