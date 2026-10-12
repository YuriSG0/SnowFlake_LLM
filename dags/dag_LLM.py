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
        @task()
        def extract_data_crosswalk():
           df = search_data(query_crosswalk)
           return df
        @task()
        def extract_data_dictionary():
            df = search_data(query_dictionary)
            return df
        @task()
        def extract_data_price():
            df = search_data(query_price)
            return df
        @task()
        def extract_data_pricesnapshot():
            df = search_data(query_pricesnapshot)
            return df
        @task()
        def extract_data_snapshot():
            df = search_data(query_snapshot)
            return df

        df_crosswalk = extract_data_crosswalk()
        df_dictionary = extract_data_dictionary()
        df_price = extract_data_price()
        df_price_snapshot = extract_data_pricesnapshot()
        df_snapshot = extract_data_snapshot()

    with TaskGroup('Transform') as transform_beachmark_LLM:
        @task()
        def header_adjust(df):
            df = header_adjustment(df)
            return df
        @task()
        def drop_column_price(df):
            df = drop_columns_price()
            return df
        @task()
        def drop_column_snapshot(df):
            df = drop_columns_snapshot(df)
            return df
        @task()
        def drop_column_price_snapshot(df):
            df = drop_columns_price_snapshot(df)
            return df

        df_crosswalk_transformed = header_adjust(df_crosswalk)
        df_dictionary_transformed = header_adjust(df_dictionary)
        df_price_transformed = drop_column_price(df_price)
        df_price_snapshot_transformed = drop_column_price_snapshot(df_price_snapshot)
        df_snapshot_transformed = drop_column_snapshot(df_snapshot)

    with TaskGroup('Load') as loading_data_LLM:
        @task()
        def load_data(df,table):
            upload_data(df,table)

        load_data(df_crosswalk_transformed,'Tb_Crosswalk')
        load_data(df_dictionary_transformed,'Tb_Dictionary')
        load_data(df_price_transformed,'Tb_Price')
        load_data(df_price_snapshot_transformed,'Tb_Price_Snaphsot')
        load_data(df_snapshot_transformed,'Tb_Snapshot')

dag_LLM_Beachmark()
    
