def generate_query(query_params={}):
    if "field" not in query_params:
        return {}
    if query_params["operator"] == "equals":
        query = {query_params["field"]: query_params["value"]}
        return query