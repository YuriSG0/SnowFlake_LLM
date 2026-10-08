import pandas as pd
from extract.extract_data import search_data
from data.connection_test import connection_snowflake
from data.sql_query import query_crosswalk,query_dictionary

def header_adjustment(df:pd.DataFrame) -> pd.DataFrame:

    df.columns = df.loc[0]
    df = df.loc[1:].reset_index(drop=False)
    return df

def drop_columns_price(df:pd.DataFrame):

    df = df.drop(columns=['BENCHMARK_SOURCE','BENCHMARK_LICENSE','SCENARIO_10K_1K_USD','ARENA_RATING_PER_USD_10K_1K'])
    return df

