"""
=====================================================
Transform CRM Customer Information
=====================================================
Script Purpose:
    This script applies the data cleansing and transformation rules for the
    'crm_cust_info' table before loading the data into the Silver layer.
    The transformations improve data quality by removing invalid records,
    eliminating duplicates, standardizing text values, and converting coded
    values into meaningful descriptions.

Notes:
    - Removes records with invalid primary keys.
    - Keeps only the most recent record for each customer.
    - Standardizes customer names by trimming leading and trailing spaces.
    - Cleans and standardizes marital status values.
    - Converts gender codes into descriptive values.
"""

import pandas as pd

def execute(table_name: str, df: pd.DataFrame) -> pd.DataFrame:

    # data type dictionary standardization
    df = df.astype(
        {
            'cst_id': 'int32[pyarrow]',
            'cst_key': 'string',
            'cst_firstname': 'string',
            'cst_lastname': 'string',
            'cst_marital_status': 'string',
            'cst_gndr': 'string',
            'cst_create_date': 'date32[pyarrow]'
        }
    )

    """
    =====================================================
    Column: cst_id
    =====================================================
    """
    # remove all lines where cst_id is null (PK)
    df = df[~df['cst_id'].isna()]

    # sort by creation date so the newest record appears first
    df = df.sort_values(by='cst_create_date', ascending=False)

    # Remove duplicate customers, keeping only the most recent record.
    df = df.drop_duplicates(subset='cst_id')

    """
    =====================================================
    Columns: cst_firstname, cst_lastname
    =====================================================
    """
    # removes leading and trailing spaces from customer names
    df['cst_firstname'] = df['cst_firstname'].transform(str.strip)
    df['cst_lastname'] = df['cst_lastname'].transform(str.strip)

    """
    =====================================================
    Column: cst_marital_status
    =====================================================
    """

    # Standardize marital status values
    df['cst_marital_status'] = df['cst_marital_status'].transform(str.upper).transform(str.strip)
    
    # Replace marital status codes with descriptive values.
    df['cst_marital_status'] = df['cst_marital_status'].case_when(
        caselist=[
            (df['cst_marital_status'].str.contains('S') ,'Single'), 
            (df['cst_marital_status'].str.contains('M'), 'Married'),
            (pd.Series(True, index=df.index), 'n/a')
        ]
    )

    """
    =====================================================
    Column: cst_gndr
    =====================================================
    """

    # replace gender codes with descriptive values
    df['cst_gndr'] = df['cst_gndr'].case_when(
        caselist=[
            (df['cst_gndr'].str.contains('F') ,'Female'), 
            (df['cst_gndr'].str.contains('M'), 'Male'),
            (pd.Series(True, index=df.index), 'n/a')
        ]
    )

    return df