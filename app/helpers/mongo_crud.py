"""Mongo DB ORM Methods"""
from uuid import uuid4
from app.utils.constants import MONGO_ID, MONGO_SET, INSERT_ONE, INSERT_MANY, FIND_ONE, FIND_MANY, DELETE_ONE, DELETE_MANY, UPDATE_ONE, UPDATE_MANY

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
    collection = __data_base[collection_name]
    if function == FIND_ONE:
        record = collection.find_one(query)
    elif function == FIND_MANY:
        record = list(collection.find(query))
    return record


def insert_record_to_collection(collection_name: str, fields: dict, function: str = INSERT_ONE):
    """Mongo Insert Method"""
    collection = __data_base[collection_name]
    if function == INSERT_ONE:
        if MONGO_ID not in fields:
            fields[MONGO_ID] = f"""{uuid4()}"""
        record = collection.insert_one(fields)
    elif function == INSERT_MANY:
        record = collection.insert_many(fields)
    return record


def update_record_in_collection(collection_name: str, fields: dict, query: dict = {}, function: str = UPDATE_ONE):
    """Mongo Update Method"""
    collection = __data_base[collection_name]
    fields = {MONGO_SET: fields}
    if function == UPDATE_ONE:
        record = collection.update_one(query, fields)
    elif function == UPDATE_MANY:
        record = collection.update_many(query, fields)
    return record


def delete_record_from_collection(collection_name: str, query: dict = {}, function: str = DELETE_ONE):
    """Mongo Delete Method"""
    collection = __data_base[collection_name]
    if function == DELETE_ONE:
        record = collection.delete_one(query)
    elif function == DELETE_MANY:
        record = collection.delete_many(query)
    return record


def get_collections_from_db():
    """This Method Gives Collection Names From DB"""
    collections = __data_base.list_collection_names()
    return collections
