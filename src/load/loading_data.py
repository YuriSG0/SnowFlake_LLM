import pandas as pd
import pyodbc
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine 
from sqlalchemy.engine import Engine
from data.connect_SQL import connection_SQL
from urllib.parse import quote_plus


def upload_data(df:pd.DataFrame,table:str):

    conn = connection_SQL()

    connection = ( "mssql+pyodbc:///?odbc_connect=" + quote_plus(conn) )

    engine = create_engine(connection)

    df.to_sql(
        name=str,
        con=engine,
        if_exists='append',
        index=False
    )

    engine.dispose()