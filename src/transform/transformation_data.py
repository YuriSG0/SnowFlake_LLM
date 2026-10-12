import pandas as pd

def header_adjustment(df:pd.DataFrame) -> pd.DataFrame:

    df.columns = df.loc[0]
    df = df.loc[1:].reset_index(drop=False)
    return df

def drop_columns_price(df:pd.DataFrame) -> pd.DataFrame:

    df = df.drop(columns=['BENCHMARK_SOURCE','BENCHMARK_LICENSE','SCENARIO_10K_1K_USD','ARENA_RATING_PER_USD_10K_1K'])
    return df

def drop_columns_snapshot(df:pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=['BENCHMARK_SOURCE','BENCHMARK_LICENSE'])
    return df

def drop_columns_price_snapshot(df:pd.DataFrame) -> pd.DataFrame:
    df = df.drpo(columns=['RETRIEVED_AT_ISO','SOURCE_URL','NOTES','IS_PROMOTIONAL','PRICE_BASIS'])
    return df

def drop_columns_llm_beachmark(df:pd.DataFrame) -> pd.DataFrame:
    df.drop(columns=[''])