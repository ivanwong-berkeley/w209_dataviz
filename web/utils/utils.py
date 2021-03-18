import numpy as np
from datetime import datetime,timedelta, date
import pandas as pd
import sqlite3
import json
import sys
import os

DB_FILE = "products.db"
for dirname in reversed(sys.path):
    candidate = os.path.join(dirname, 'products.db')
    print(candidate)
    if os.path.isfile(candidate):
        DB_FILE = candidate
        break
print("DB_FILE " + DB_FILE) 

#loading data
def load_data():

    # Read sqlite query results into a pandas DataFrame
    # con = sqlite3.connect("amzn-products.db")
    con = sqlite3.connect(DB_FILE)

    df = pd.read_sql_query("SELECT * from product ", con)

    # Verify that result of SQL query is stored in the dataframe
    # print(df.head(5))

    con.close()

    return df

def load_category_data(category_name):

    # Read sqlite query results into a pandas DataFrame

    # con = sqlite3.connect("amzn-products.db")
    con = sqlite3.connect("products.db")

    sql = 'select * from product where category = "{}"'.format(category_name)

    df = pd.read_sql_query(sql, con)

    # Verify that result of SQL query is stored in the dataframe
    # print(df.head(5))

    con.close()

    return df

def clean_numeric_data(x):
    # If the value is a string, then remove currency symbol, delimiters, and N.A.
    # otherwise, the value is numeric and can be converted

    if isinstance(x, str):
        return(x.replace('$', '').replace(',', '').replace('N.A.','0').replace('--','0').replace('< ','-'))
    return(x)


## Data Cleaning
def clean_data(df):
    # Trim spaces in all columns in the dataframe

    def trim_all_columns(df):
        # Trim whitespace from ends of each value across all series in dataframe
        trim_strings = lambda x: x.strip() if isinstance(x, str) else x
        return df.applymap(trim_strings)

    # simple example of trimming whitespace from data elements
    df = trim_all_columns(df)
    # print(df)

    ### Fixing Rank column
    df['Rank'].apply(type)

    # Check Data Type in Rank
    # See different data types in the same column.
    # df['Rank'].apply(type).value_counts()

    # Clean data and convert to float data type
    df['Rank'] = df['Rank'].apply(clean_numeric_data).astype('float')

    # Check Data Type in Rank
    # See float data types in the column.
    df['Rank'].apply(type).value_counts()

    ### Fixing Est_Monthly_Revenue, Est_Monthly_Sales, Fees, and Net columns

    # Check Data Type in Est_Monthly_Revenue
    # See different data types in the same column.
    df['Est_Monthly_Revenue'].apply(type)

    # Check Data Type in Est_Monthly_Revenue
    # See different data types in the same column.
    df['Est_Monthly_Revenue'].apply(type).value_counts()

    # Clean data and convert to float data type
    df['Price'] = df['Price'].apply(clean_numeric_data).astype('float')

    # Clean data and convert to float data type
    df['Est_Monthly_Revenue'] = df['Est_Monthly_Revenue'].apply(clean_numeric_data).astype('float')

    # Clean data and convert to float data type
    df['Est_Monthly_Sales'] = df['Est_Monthly_Sales'].apply(clean_numeric_data).astype('float')

    # Clean data and convert to float data type
    df['Fees'] = df['Fees'].apply(clean_numeric_data).astype('float')

    # Clean data and convert to float data type
    df['Net'] = df['Net'].apply(clean_numeric_data).astype('float')

    # Check Data Type in Est_Monthly_Revenue
    # See float data types in the column.
    df['Est_Monthly_Revenue'].apply(type).value_counts()

    # Clean data and convert to float data type
    df['Reviews'] = df['Reviews'].apply(clean_numeric_data).astype('float')

    df.Est_Monthly_Revenue

    return df

