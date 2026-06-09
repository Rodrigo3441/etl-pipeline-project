# database connector
# this file will return a connection objetc
# author: rodrigo
# date: June 8th 2026

import mysql.connector

def get_connection():
    try:
        return (mysql.connector.Connect(
                user='root',
                password='root', 
                host='127.0.0.1',
                database='solucxData'))
    except mysql.connector.Error as error:
        print(f"Database connection error: {error}")
        raise
