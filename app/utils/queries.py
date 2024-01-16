"""Query Methods"""
from app.utils.constants import FIELD, OPERATOR, EQUALS, VALUE


def generate_query(query_params={}):
    """This Method Provides Query For Mongo DB Operations"""
    try:
        if FIELD not in query_params:
            return {}
        if query_params.get(OPERATOR, None) == EQUALS:
            query = {query_params[FIELD]: query_params[VALUE]}
            return query
    except Exception as ex:
        print(ex)
        return ex
