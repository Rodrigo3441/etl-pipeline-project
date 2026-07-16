"""
=====================================================
Transform ERP Customer Location Information
=====================================================
Script Purpose:
    This script applies the data cleansing and transformation rules for the
    'erp_loc_a101' table before loading the data into the Silver layer.
    The transformations improve data quality by standardizing data types,
    cleaning customer identifiers, and standardizing country values.

Notes:
    - Standardizes column data types.
    - Removes invalid characters from customer identifiers.
    - Removes leading and trailing spaces from country values.
    - Replaces country codes and missing values with meaningful names.
"""

import pandas as pd

def execute(df: pd.DataFrame) -> pd.DataFrame:

    # data type dictionary standardization
    df = df.astype(
        {
            'cid': 'string',
            'cntry': 'string'
        }
    )

    """
    =====================================================
    Column: cid
    =====================================================
    """ 
    # remove invalid characters from the column
    df['cid'] = df['cid'].str.replace('-', '')

    """
    =====================================================
    Column: cntry
    =====================================================
    """ 
    # remove leading and trailing spaces
    df['cntry'] = df['cntry'].str.strip()

    # replace country codes with meaningful names
    df['cntry'] = df['cntry'].case_when(
        caselist=[
            (
                ((df['cntry'] == '') | (df['cntry'].isna())),
                'n/a'
            ),
            (
                (df['cntry'].str.upper().isin(('USA', 'US'))),
                'United States'
            ),
            (
                (df['cntry'].str.upper() == 'DE'),
                'Germany'
            ) 
        ]
    )

    return df