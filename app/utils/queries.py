"""Query Methods"""


def generate_query(query_params={}):
    """This Method Provides Query For Mongo DB Operations"""
    try:
        if "field" not in query_params:
            return {}
        if query_params["operator"] == "equals":
            query = {query_params["field"]: query_params["value"]}
            return query
    except Exception as ex:
        print(ex)
        return ex
