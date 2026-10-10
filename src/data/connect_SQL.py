from dotenv import load_dotenv
import pyodbc
import os
from pathlib import Path
from typing import Optional

load_dotenv(Path(__file__).resolve().parent.parent.parent / 'config' / '.env')

def connection_SQL() -> Optional[pyodbc.Connection]:

    try : 
        conection = (
            f"DRIVER={os.getenv('Driver')};"
            f"SERVER={os.getenv('Server')};"
            f"DATABASE={os.getenv('Database_Sink')};"
            f"UID={os.getenv('User_SQL')};"
            f"PWD={os.getenv('Password_SQL')};"
            "TrustServerCertificate=yes;"
            )

        conn = pyodbc.connect(conection)

        return conn
    
    except Exception as e:
        print(f'Erro crítico ao ligar ao SQL: {e}')
        return False


