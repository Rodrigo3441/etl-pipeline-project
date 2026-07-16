"""
=====================================================
Transform ERP Product Categories
=====================================================
Script Purpose:
    This script prepares the 'erp_px_cat_g1v2' table for the Silver layer.
    The source data is already clean and consistent, therefore no data
    transformations are required beyond standardizing the column data types.

Notes:
    - Standardizes column data types.
    - No additional data cleansing or transformation rules are required.
"""

import pandas as pd
import sys

def execute(df: pd.DataFrame) -> pd.DataFrame:

    # data type dictionary standardization
    df = df.astype(
        {
            'id': 'string',
            'cat': 'string',
            'subcat': 'string',
            'maintenance': 'string'
        }
    )

    # no data transformations needed for this source

    return df