"""
=====================================================
Transform CRM Product Information
=====================================================
Script Purpose:
    This script applies the data cleansing and transformation rules for the
    'crm_prd_info' table before loading the data into the Silver layer.
    The transformations improve data quality by standardizing data types,
    deriving new columns, replacing coded values, handling missing values,
    and calculating product validity periods.

Notes:
    - Standardizes column data types.
    - Extracts the product category identifier from the product key.
    - Replaces missing product costs with zero.
    - Converts product line codes into descriptive values.
    - Calculates the product end date based on the next available
      product version.
"""

import pandas as pd
from datetime import timedelta

def execute(table_name: str, df: pd.DataFrame) -> pd.DataFrame:
   
    # data type dictionary standardization
    df = df.astype(
        {
            'prd_id': 'int32[pyarrow]',
            'prd_key': 'string',
            'prd_nm': 'string',
            'prd_cost': 'int32[pyarrow]',
            'prd_line': 'string',
            'prd_start_dt': 'datetime64[s]',
            'prd_end_dt':   'datetime64[s]'
        }
    )

    """
    =====================================================
    Column: prd_key, cat_id
    =====================================================
    """ 
    # derive a new column called 'cat_id', extracted from the first 4 characters of the existing column
    df.insert(1, 'cat_id', df['prd_key'].str[:5])

    # remove the first 5 characters from the column
    df['prd_key'] = df['prd_key'].str[6:]

    # replace null prices with zero
    df['prd_cost'] = df['prd_cost'].case_when(
        caselist=[
            (pd.isna, 0)
            ]
        )

    """
    =====================================================
    Column: prd_line
    =====================================================
    """
    # replace name codes with meaningful information
    df['prd_line'] = df['prd_line'].case_when(
        caselist=[
            (df['prd_line'].str.contains('M'), 'Mountain'),
            (df['prd_line'].str.contains('R'), 'Road'),
            (df['prd_line'].str.contains('S'), 'Other Sales'),
            (df['prd_line'].str.contains('T'), 'Touring'),
            (pd.Series(True, index=df.index), 'n/a')
        ]
    )

    """
    =====================================================
    Column: prd_end_dt
    =====================================================
    """
    # Sort products by name and start date
    df = df.sort_values(by=['prd_nm','prd_start_dt'])

    # Get the next start date for each product as the new end date
    df['prd_end_dt'] = df.groupby('prd_key')['prd_start_dt'].shift(-1)

    # Set end date as one day before the next start date
    df['prd_end_dt'] = df['prd_end_dt'] - timedelta(days=1)

    return df
    