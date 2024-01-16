"""Mongo DB Routes"""
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.helpers.token_manager import is_token_valid
from app.helpers.mongo_crud import get_record_from_collection, insert_record_to_collection, update_record_in_collection, delete_record_from_collection, get_collections_from_db, get_pre_defined_queries_list
from app.utils.constants import COLLECTION_NAMES, MESSAGE, RECORDS, USER, INSERT_MANY, FIND_MANY, DELETE_MANY, UPDATE_MANY, QUERIES
from app.utils.validators import CrudRequest
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
        MESSAGE: "Collection Names Retrieved From The Data Base Successfully"
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
        MESSAGE: "Records Retrieved From The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.post("/records")
async def insert_records(payload: CrudRequest):
    """Insert Records Endpoint"""
    payload.fields = add_uuid_to_records(payload.dict().get("fields"))
    records = insert_record_to_collection(
        payload.collection_name, payload.fields, function=INSERT_MANY)
    response = {
        MESSAGE: "Records Inserted to The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.put("/records")
async def update_records(payload: CrudRequest):
    """Update Records Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    records = update_record_in_collection(
        payload.collection_name, payload.fields,  query, UPDATE_MANY)
    response = {
        MESSAGE: "Records Updated To The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.delete("/records")
async def delete_records(payload: CrudRequest):
    """Delete Records Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    records = delete_record_from_collection(
        payload.collection_name, query, DELETE_MANY)
    response = {
        MESSAGE: "Records Deleted From The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.get("/record/{collection_name}")
async def get_record(payload: CrudRequest = Depends()):
    """Get Record Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    record = get_record_from_collection(payload.collection_name, query)
    response = {
        RECORDS: [record],
        MESSAGE: "Record Retrieved From The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.post("/record")
async def insert_record(payload: CrudRequest):
    """Insert Record Endpoint"""
    record = insert_record_to_collection(**payload.dict(exclude_none=True))
    response = {
        MESSAGE: "Record Inserted To The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.put("/record")
async def update_record(payload: CrudRequest):
    """Update Record Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    record = update_record_in_collection(
        payload.collection_name, payload.fields,  query)
    response = {
        MESSAGE: "Record Updated To The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.delete("/record")
async def delete_record(payload: CrudRequest):
    """Delete Record Endpoint"""
    query = generate_query(payload.dict(exclude_none=True))
    record = delete_record_from_collection(payload.collection_name, query)
    response = {
        MESSAGE: "Record Deleted From The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.get("/pre-defined-queries")
async def get_pre_defined_queries():
    """Get Pre Defined Queries Endpoint"""
    queries = get_pre_defined_queries_list()
    response = {
        QUERIES: queries,
        MESSAGE: "Pre Defined Queries Retrieved Successfully"
    }
    return JSONResponse(content=response)
