from src.data.expanses_repository import get_all_records, get_fields, query_records
from src.util.request_utils import params_to_query


def query_data(params: dict = None):
    if not params:
        return get_all_records()
    else:
        query_string = params_to_query(params)
        return query_records(query_string)
