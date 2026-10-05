from snowflake.connector import SnowflakeConnection
import snowflake.connector 
from dotenv import load_dotenv
from pathlib import Path
import os
from typing import Optional

load_dotenv(Path(__file__).resolve().parent.parent.parent / 'config' / '.env')

def connection_snowflake() -> Optional[SnowflakeConnection]:
    try: 
        conn = snowflake.connector.connect(
        user=os.getenv('Login'),
        password=os.getenv('Password'),
        account=os.getenv('Account'),
        warehouse=os.getenv('Warehouse'),
        database=os.getenv('Database'),
        schema=os.getenv('Schema')
        )

        return conn

    except :

        return False

