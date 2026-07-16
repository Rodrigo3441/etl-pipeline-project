"""
=====================================================
Transform CRM Sales Details
=====================================================
Script Purpose:
    This script applies the data cleansing and transformation rules for the
    'crm_sales_details' table before loading the data into the Silver layer.
    The transformations improve data quality by standardizing data types,
    converting date columns, and correcting invalid sales and price values.

Notes:
    - Standardizes column data types.
    - Converts integer-based dates into datetime format.
    - Recalculates invalid sales amounts using quantity and price.
    - Derives missing or invalid product prices from sales and quantity.
"""

import pandas as pd
import numpy as np

def execute(df: pd.DataFrame) -> pd.DataFrame:

    # data type dictionary standardization
    df = df.astype(
        {
            'sls_ord_num'    : 'string',
            'sls_prd_key'    : 'string',
            'sls_cust_id'    : 'int32[pyarrow]',
            'sls_order_dt'   : 'int32[pyarrow]',
            'sls_ship_dt'    : 'int32[pyarrow]',
            'sls_due_dt'     : 'int32[pyarrow]',
            'sls_sales'      : 'int32[pyarrow]',
            'sls_quantity'   : 'int32[pyarrow]',
            'sls_price'      : 'int32[pyarrow]',
        }
    )

    """
    =====================================================
    Columns: sls_order_dt, sls_ship_dt, sls_due_dt
    =====================================================
    """ 
    # convert all dates from int format to a proper date format
    df['sls_order_dt'] = pd.to_datetime(df['sls_order_dt'], errors='coerce', format='%Y%m%d')
    df['sls_ship_dt'] = pd.to_datetime(df['sls_ship_dt'], errors='coerce', format='%Y%m%d')
    df['sls_due_dt'] = pd.to_datetime(df['sls_due_dt'], errors='coerce', format='%Y%m%d')
    
    """
    =====================================================
    Column: sls_quantity
    =====================================================
    """ 
    # fix data quality issues related to sls_sales column and reevaluate the calculus if necessary
    df['sls_sales'] = df['sls_sales'].case_when(
        caselist=[
            (
                (df['sls_sales'].isna()) | 
                (df['sls_sales'] <= 0) | 
                (df['sls_sales'] != df['sls_quantity'] * df['sls_price'].abs()), 
                (df['sls_quantity'] * df['sls_price'].abs()) # replace sls_sales with quantity * price columns
            )
        ]
    )

    """
    =====================================================
    Column: sls_price
    =====================================================
    """ 
    #  derive price if original value is invalid
    df['sls_price'] = df['sls_price'].case_when(
        caselist=[
            (
                (df['sls_price'].isna()) |
                (df['sls_price'] <= 0),
                (df['sls_sales'] / df['sls_quantity'])
                    .where(df['sls_quantity'] != 0, np.nan)
                    .astype('int32[pyarrow]')
            )
        ]
    )

    return df