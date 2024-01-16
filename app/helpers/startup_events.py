"""StartUP Methods"""
from pymongo import MongoClient
from app.helpers.mongo_orm import set_mongo_db_connection
from app.utils.config import MONGO_CLIENT_URI


def connect_to_mongo_db():
    """This Method Establishes Connection To Mongo DB"""
    client = MongoClient(MONGO_CLIENT_URI, directConnection=True)
    set_mongo_db_connection(client)
