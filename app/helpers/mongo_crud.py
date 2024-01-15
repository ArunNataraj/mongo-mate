from uuid import uuid4
from app.utils.constants import MONGO_ID, MONGO_SET, INSERT_ONE, INSERT_MANY, FIND_ONE, FIND_MANY, DELETE_ONE, DELETE_MANY

__mongo_db_client = None
__data_base = None


def set_mongo_db_connection(mongo_db_client):
    global __mongo_db_client, __data_base
    __mongo_db_client = mongo_db_client
    __data_base = mongo_db_client.get_database()
    print(__mongo_db_client)
    print(__data_base)


def get_record_from_collection(collection_name: str, query: dict = {}, function=FIND_ONE):
    collection = __data_base[collection_name]
    if function == FIND_ONE:
        record = collection.find_one(query)
    elif function == FIND_MANY:
        record = list(collection.find(query))
    return record


def insert_record_to_collection(collection_name, fields, function=INSERT_ONE):
    collection = __data_base[collection_name]
    if function == INSERT_ONE:
        if MONGO_ID not in fields:
            fields[MONGO_ID] = f"""{uuid4()}"""
        record = collection.insert_one(fields)
    elif function == INSERT_MANY:
        record = collection.insert_many(fields)
    return record


def update_record_in_collection(collection_name, query, fields):
    collection = __data_base[collection_name]
    fields = {MONGO_SET: fields}
    record = collection.update_one(query, fields)
    return record


def delete_record_from_collection(collection_name, query: dict = dict, function=DELETE_ONE):
    collection = __data_base[collection_name]
    if function == DELETE_ONE:
        record = collection.delete_one(query)
    elif function == DELETE_MANY:
        record = collection.delete_many(query)
    return record


def get_collections_from_db():
    collections = __data_base.list_collection_names()
    return collections
