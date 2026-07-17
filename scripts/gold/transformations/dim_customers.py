"""
=====================================================
Build Customer Dimension
=====================================================
Script Purpose:
    This script builds the Customer Dimension (`dim_customers`) for the
    Gold layer by combining customer information from multiple Silver
    tables into a single business-ready DataFrame.

Notes:
    - Removes technical Data Warehouse columns.
    - Merges customer information from CRM and ERP sources.
    - Enriches missing customer attributes using ERP data.
    - Creates a surrogate key for analytical purposes.
    - Renames and reorders columns to produce the final
      Customer Dimension.
"""

import pandas as pd

def execute(
        crm_cust_info: pd.DataFrame, 
        erp_cust_az12: pd.DataFrame, 
        erp_loc_a101: pd.DataFrame
    ) -> dict:

    # remove the data warehouse column information 
    crm_cust_info = crm_cust_info.drop('dwh_create_date', axis=1)
    erp_cust_az12 = erp_cust_az12.drop('dwh_create_date', axis=1)
    erp_loc_a101 = erp_loc_a101.drop('dwh_create_date', axis=1)

    # merge the customer info dataframe with others two dataframes that provides more information
    result = pd.merge(crm_cust_info, erp_cust_az12, how='left', left_on='cst_key', right_on='cid')
    result = pd.merge(result, erp_loc_a101, how='left', left_on='cst_key', right_on='cid')

    # remove duplicated columns of customer id
    result = result.drop('cid_x', axis=1)
    result = result.drop('cid_y', axis=1)
    
    # enhance information about the gender that is not available on the first dataframe
    result['cst_gndr'] = result['cst_gndr'].case_when(
        caselist=[
            (
                (result['cst_gndr'] == 'n/a') & (~result['gen'].isna()),
                result['gen']
            ),
            (                
                (result['gen'].isna()),
                'n/a'
            )
        ]
    )

    # remove the extra gender column after gender data enhancement
    result = result.drop('gen', axis=1)

    # sort the data by the customer id before creating a new primary key for data aggregations
    result = result.sort_values(by='cst_id', ascending=True)

    # create a primary key column for data aggregations
    result['customer_key'] = range(1, len(result) + 1)

    # renaming columns for meaningful names
    result = result.rename(
        columns={
            'cst_id': 'customer_id',
            'cst_key': 'customer_number',
            'cst_firstname': 'first_name',
            'cst_lastname': 'last_name',
            'cst_marital_status': 'marital_status',
            'cst_gndr': 'gender',
            'cst_create_date': 'create_date',
            'bdate': 'birthdate',
            'cntry': 'country'
        }
    )

    # reorder columns to improve consistency
    result = result[
        [
            'customer_key',
            'customer_id',
            'customer_number',
            'first_name',
            'last_name',
            'country',
            'marital_status',
            'gender',
            'birthdate',
            'create_date'
        ]
    ]

    return result