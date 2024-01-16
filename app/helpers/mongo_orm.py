"""Mongo DB ORM Methods"""
from fastapi import HTTPException
from uuid import uuid4
from pymongo import ASCENDING, DESCENDING
from app.utils.constants import (MONGO_ID, MONGO_SET, INSERT_ONE, INSERT_MANY, FIND_ONE, FIND_MANY,
                                 DELETE_ONE, DELETE_MANY, UPDATE_ONE, UPDATE_MANY,
                                 PRE_DEFINED_QUERIES,
                                 QUERY1, QUERY2, QUERY3, QUERY4, QUERY5, QUERY6)

__mongo_db_client = None
__data_base = None


def set_mongo_db_connection(mongo_db_client):
    """Mongo DB Connection"""
    global __mongo_db_client, __data_base
    __mongo_db_client = mongo_db_client
    __data_base = mongo_db_client.get_database()
    print(__mongo_db_client)
    print(__data_base)


def get_record_from_collection(collection_name: str, query: dict = {}, function: str = FIND_ONE):
    """Mongo Get Method"""
    try:
        collection = __data_base[collection_name]
        if function == FIND_ONE:
            record = collection.find_one(query)
        elif function == FIND_MANY:
            record = list(collection.find(query))
        return record
    except Exception as ex:
        print(ex)
        return ex


def insert_record_to_collection(collection_name: str, fields: dict, function: str = INSERT_ONE):
    """Mongo Insert Method"""
    try:
        collection = __data_base[collection_name]
        if function == INSERT_ONE:
            if MONGO_ID not in fields:
                fields[MONGO_ID] = f"""{uuid4()}"""
            record = collection.insert_one(fields)
        elif function == INSERT_MANY:
            record = collection.insert_many(fields)
        return record
    except Exception as ex:
        print(ex)
        return ex


def update_record_in_collection(collection_name: str, fields: dict, query: dict = {}, function: str = UPDATE_ONE):
    """Mongo Update Method"""
    try:
        collection = __data_base[collection_name]
        fields = {MONGO_SET: fields}
        if function == UPDATE_ONE:
            record = collection.update_one(query, fields)
        elif function == UPDATE_MANY:
            record = collection.update_many(query, fields)
        return record
    except Exception as ex:
        print(ex)
        return ex


def delete_record_from_collection(collection_name: str, query: dict = {}, function: str = DELETE_ONE):
    """Mongo Delete Method"""
    try:
        collection = __data_base[collection_name]
        if function == DELETE_ONE:
            record = collection.delete_one(query)
        elif function == DELETE_MANY:
            record = collection.delete_many(query)
        return record
    except Exception as ex:
        print(ex)
        return ex


def get_collections_from_db():
    """This Method Gives Collection Names From DB"""
    try:
        collections = __data_base.list_collection_names()
        return collections
    except Exception as ex:
        print(ex)
        return ex


def get_pre_defined_queries_list():
    """This Method Gives list of Predefined Queries"""
    return PRE_DEFINED_QUERIES


def query_executor(data):
    """This method Executes Pre Defined Queries"""
    collection = __data_base[data.collection_name]
    query = data.pre_defined_query

    if query == QUERY1:
        if not data.collection_name:
            raise HTTPException(
                status_code=422, detail="query_executor: query1: missing collection name")

        insert_record_to_collection(data.collection_name, {})
        delete_record_from_collection(data.collection_name)
        return f"Created Collection Named '{data.collection_name}'."

    elif query == QUERY2:
        if not data.field:
            raise HTTPException(
                status_code=422, detail="query_executor: query2: missing field name")

        index = collection.create_index(data.field, unique=True)
        return f"""Created Index '{index}' with the specified Field '{data.field}' in the Collection '{data.collection_name}'."""

    elif query == QUERY3 or query == QUERY4:
        if not data.field:
            raise HTTPException(
                status_code=422, detail=f"query_executor: {query}: missing field name")

        sort_direction = ASCENDING if query == QUERY3 else DESCENDING
        records = collection.find().sort(data.field, sort_direction)
        return list(records)

    elif query == QUERY5:
        if not data.limit_count:
            raise HTTPException(
                status_code=422, detail="query_executor: query5: missing limit count")

        records = collection.find().limit(data.limit_count)
        return list(records)

    elif query == QUERY6:
        if not data.fields:
            raise HTTPException(
                status_code=422, detail="query_executor: query6: missing field names")

        fields = {field: 1 for field in data.fields}
        records = collection.find({}, fields)
        return list(records)

    else:
        raise HTTPException(
            status_code=400, detail="query_executor: no such pre-defined queries")
