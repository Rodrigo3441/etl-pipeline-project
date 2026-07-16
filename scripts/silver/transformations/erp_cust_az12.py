"""
=====================================================
Transform ERP Customer Information
=====================================================
Script Purpose:
    This script applies the data cleansing and transformation rules for the
    'erp_cust_az12' table before loading the data into the Silver layer.
    The transformations improve data quality by standardizing data types,
    cleaning customer identifiers, validating birth dates, and
    standardizing gender values.

Notes:
    - Standardizes column data types.
    - Removes the 'NAS' prefix from customer identifiers.
    - Replaces invalid future birth dates with null values.
    - Standardizes gender values into descriptive names.
"""

import pandas as pd
import datetime

def execute(df: pd.DataFrame) -> pd.DataFrame:

    # data type dictionary standardization
    df = df.astype(
        {
            'cid': 'string',
            'bdate': 'date32[pyarrow]',
            'gen': 'string',
        }
    )

    """
    =====================================================
    Column: cid
    =====================================================
    """ 
    # remove the prefix NAS from cid column
    df['cid'] = df['cid'].case_when(
        caselist=[
            (
                df['cid'].str.startswith('NAS'),
                df['cid'].str[3:]
            )
        ]
    )

    """
    =====================================================
    Column: bdate
    =====================================================
    """ 
    df['bdate'] = df['bdate'].case_when(
        caselist=[
            (
                df['bdate'] > datetime.date.today(),
                pd.NA
            )
        ]
    )

    """
    =====================================================
    Column: gen
    =====================================================
    """ 
    # standardize gender informations to uppercase
    df['gen'] = df['gen'].str.upper()
    
    # remove leading and trailing spaces from gender information
    df['gen'] = df['gen'].str.strip()

    # replace gender code names with meaningful information    
    df['gen'] = df['gen'].case_when(
        caselist=[
            (
                df['gen'].isin(('F', 'FEMALE')),
                'Female'
            ),
            (
                df['gen'].isin(('M', 'MALE')),
                'Male'
            ),
            (
                pd.Series(True, index=df.index),
                'n/a'
            )
        ]
    )

    return df