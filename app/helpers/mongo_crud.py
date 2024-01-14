from uuid import uuid4
from app.utils.constants import MONGO_ID, MONGO_SET

__mongo_db_client = None
__data_base = None


def set_mongo_db_connection(mongo_db_client):
    global __mongo_db_client, __data_base
    __mongo_db_client = mongo_db_client
    __data_base = mongo_db_client.get_database()
    print(__mongo_db_client)
    print(__data_base)


def get_records_from_collection(collection_name: str, query: dict = {}):
    collection = __data_base[collection_name]
    records = list(collection.find(query))
    print(records)
    return records


def get_record_from_collection(collection_name: str, query: dict = {}):
    collection = __data_base[collection_name]
    record = collection.find_one(query)
    return record


def insert_record_to_collection(collection_name, fields):
    if MONGO_ID not in fields:
        fields[MONGO_ID] = f"""{uuid4()}"""
    collection = __data_base[collection_name]
    record = collection.insert_one(fields)
    return record


def update_record_in_collection(collection_name, query, fields):
    collection = __data_base[collection_name]
    fields = {MONGO_SET: fields}
    record = collection.update_one(query, fields)
    return record


def delete_record_from_collection(collection_name, fields):
    collection = __data_base[collection_name]
    record = collection.find_one_and_delete(fields)
    return record


def get_collections_from_db():
    collections = __data_base.list_collection_names()
    return collections
