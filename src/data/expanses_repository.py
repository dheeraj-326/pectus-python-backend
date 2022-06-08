import pandas
from flask import g
from src.config.constants import CSV_PATH
from src.util.caching import cache


def get_df():
    if 'df' not in g:
        g.df = pandas.read_csv(CSV_PATH)
    return g.df


# @cache.cached()
def get_all_records():
    df = get_df()
    return df.to_dict(orient='records')


# @cache.cached(key_prefix='query_records')
def query_records(query_string):
    df = get_df()
    results = df.query(query_string, inplace=False)
    return results.to_dict(orient='records')


# @cache.cached()
def get_fields():
    return get_df().columns.values




