def extract():
    try:
        conn = get_connection()

        if (conn.is_connected()):
            print('connection stabilized!')

    except Exception as e:
        print(f'ETL failed: {e}')