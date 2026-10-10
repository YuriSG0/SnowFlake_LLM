import snowflake.connector
from snowflake.connector import SnowflakeConnection
from src.data.connect_Snowflake import connection_snowflake
from src.data.sql_query import *
import os
from pathlib import Path
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv(Path(__file__).resolve().parent.parent / 'config' / '.env')

def search_data(query=str) -> pd.DataFrame:

    conn = connection_snowflake()
    
    cursor = conn.cursor()

    cursor.execute(query)

    df = cursor.fetch_pandas_all()

    return df


