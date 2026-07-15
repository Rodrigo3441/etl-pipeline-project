import pandas as pd
import sys

def execute(df):

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

    print(df)
    sys.exit()
    return df