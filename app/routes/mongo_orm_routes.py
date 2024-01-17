"""Mongo DB Routes"""
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.helpers.token_manager import is_token_valid
from app.helpers.mongo_orm import (get_record_from_collection, insert_record_to_collection,
                                   update_record_in_collection, delete_record_from_collection,
                                   get_collections_from_db, get_pre_defined_queries_list,
                                   query_executor)
from app.utils.constants import (COLLECTION_NAMES, MESSAGE, RECORDS, USER, INSERT_MANY, FIND_MANY,
                                 DELETE_MANY, UPDATE_MANY, QUERIES, QUERY_EXC_MSG,
                                 QUERY_RETRIEVED_MSG,
                                 RECORD_DELETED_MSG, RECORD_UPDATED_MSG, RECORD_INSERTED_MSG,
                                 RECORD_RETRIEVE_MSG, COLLECTION_MSG, MONGO_ID)
from app.utils.validators import CrudRequest, ExcuteQueryRequest
from app.utils.utils import add_uuid_to_records
from app.utils.queries import generate_query

crud_router = APIRouter(dependencies=[Depends(is_token_valid)])


@crud_router.get("/collections")
async def get_collections():
    """Get Collection Names Endpoint"""
    collections = get_collections_from_db()
    collections.remove(USER)
    response = {
        COLLECTION_NAMES: collections,
        MESSAGE: COLLECTION_MSG
    }
    return JSONResponse(content=response)


@crud_router.get("/records/{collection_name}")
async def get_records(payload: CrudRequest = Depends()):
    """Get Records Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    records = get_record_from_collection(
        payload.collection_name, query, FIND_MANY)
    response = {
        RECORDS: records,
        MESSAGE: RECORD_RETRIEVE_MSG
    }
    return JSONResponse(content=response)


@crud_router.post("/records")
async def insert_records(payload: CrudRequest):
    """Insert Records Endpoint"""
    payload.fields = add_uuid_to_records(payload.dict().get("fields"))
    records = insert_record_to_collection(
        payload.collection_name, payload.fields, INSERT_MANY)
    records = get_record_from_collection(
        payload.collection_name, {MONGO_ID: {"$in": records.inserted_ids}}, FIND_MANY)
    response = {
        RECORDS: records,
        MESSAGE: RECORD_INSERTED_MSG
    }
    return JSONResponse(content=response)


@crud_router.put("/records")
async def update_records(payload: CrudRequest):
    """Update Records Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    records = update_record_in_collection(
        payload.collection_name, payload.fields,  query, UPDATE_MANY)
    records = get_record_from_collection(
        payload.collection_name, query, FIND_MANY)
    response = {
        RECORDS: records,
        MESSAGE: RECORD_UPDATED_MSG
    }
    return JSONResponse(content=response)


@crud_router.delete("/records")
async def delete_records(payload: CrudRequest):
    """Delete Records Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    deleted_records = get_record_from_collection(
        payload.collection_name, query, FIND_MANY)
    records = delete_record_from_collection(
        payload.collection_name, query, DELETE_MANY)
    response = {
        RECORDS: [] if records.deleted_count == 0 else deleted_records,
        MESSAGE: RECORD_DELETED_MSG
    }
    return JSONResponse(content=response)


@crud_router.get("/record/{collection_name}")
async def get_record(payload: CrudRequest = Depends()):
    """Get Record Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    record = get_record_from_collection(payload.collection_name, query)
    response = {
        RECORDS: [record],
        MESSAGE: RECORD_RETRIEVE_MSG
    }
    return JSONResponse(content=response)


@crud_router.post("/record")
async def insert_record(payload: CrudRequest):
    """Insert Record Endpoint"""
    record = insert_record_to_collection(**payload.dict(exclude_none=True))
    record = get_record_from_collection(
        payload.collection_name, {MONGO_ID: record.inserted_id})
    response = {
        RECORDS: [record],
        MESSAGE: RECORD_INSERTED_MSG
    }
    return JSONResponse(content=response)


@crud_router.put("/record")
async def update_record(payload: CrudRequest):
    """Update Record Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    record = update_record_in_collection(
        payload.collection_name, payload.fields,  query)
    record = get_record_from_collection(
        payload.collection_name, query)
    response = {
        RECORDS: [record],
        MESSAGE: RECORD_UPDATED_MSG
    }
    return JSONResponse(content=response)


@crud_router.delete("/record")
async def delete_record(payload: CrudRequest):
    """Delete Record Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    deleted_record = get_record_from_collection(
        payload.collection_name, query)
    record = delete_record_from_collection(payload.collection_name, query)
    response = {
        RECORDS: [] if record.deleted_count == 0 else [deleted_record],
        MESSAGE: RECORD_DELETED_MSG
    }
    return JSONResponse(content=response)


@crud_router.get("/pre-defined-queries")
async def get_pre_defined_queries():
    """Get Pre Defined Queries Endpoint"""
    queries = get_pre_defined_queries_list()
    response = {
        QUERIES: queries,
        MESSAGE: QUERY_RETRIEVED_MSG
    }
    return JSONResponse(content=response)


@crud_router.post("/execute-pre-defined-queries")
async def execute_pre_defined_queries(payload: ExcuteQueryRequest):
    """Execute Defined Queries Endpoint"""
    records = query_executor(payload)
    response = {
        RECORDS: records,
        MESSAGE: QUERY_EXC_MSG
    }
    return JSONResponse(content=response)
