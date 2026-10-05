from data import sql_query
from extract.connection_test import connection_snowflake
from extract.extract_data import search_data

conn = connection_snowflake()
query = sql_query.query_crosswalk

df = search_data(conn,query)

print(df)
