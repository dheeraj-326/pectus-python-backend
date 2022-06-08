import pandas
from flask import g

from src.config.constants import CSV_PATH


def get_df():
    if 'df' not in g:
        g.df = pandas.read_csv(CSV_PATH)
    return g.df


def get_all_records():
    df = get_df()
    return df.to_dict(orient='records')



