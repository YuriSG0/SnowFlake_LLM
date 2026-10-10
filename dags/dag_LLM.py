from datetime import datetime
import pendulum
from airflow.utils.task_group import TaskGroup
from airflow.utils.trigger_rule import TriggerRule
from airflow.decorators import task,dag
from src.extract.extract_data import search_data
from src.transform.transformation_data import *
from src.load.loading_data import upload_data
from src.data.sql_query import *

@dag(
    dag_id = 'dag_LLM_Beachmark',
    description = 'A DAG developed to capture LLM Benchmark data stored in Snowflake',
    start_date= pendulum.datetime(2026,10,10,tz='America/Sao_Paulo'),
    catchup = False,
    schedule = None,
    tags = ['SnowFlake','LLM','Beachmark']
)
def dag_LLM_Beachmark():
    with TaskGroup('Extract') as extract_beachmark_LLM:

        def extract_data_crosswalk():
           df = search_data(query_crosswalk)
           return df

        def extract_data_dictionary():
            df = search_data(query_dictionary)
            return df

        def extract_data_price():
            df = search_data(query_price)
            return df

        def extract_data_pricesnapshot():
            df = search_data(query_pricesnapshot)
            return df

        def extract_data_snapshot():
            df = search_data(query_snapshot)
            return df

    with TaskGroup('Transform') as transform_beachmark_LLM:

    
