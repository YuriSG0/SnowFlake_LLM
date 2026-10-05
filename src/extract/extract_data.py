import snowflake.connector
from snowflake.connector import SnowflakeConnection
import os
from pathlib import Path
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv(Path(__file__).resolve().parent.parent/ 'config' / '.env')

def search_data(conection_snowflake=SnowflakeConnection,query=str) -> pd.DataFrame:
    
    cursor = conection_snowflake.cursor()

    cursor.execute(query)

    df = cursor.fetch_pandas_all()

    return df