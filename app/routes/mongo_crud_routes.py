from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from app.helpers.token_manager import is_token_valid
from app.helpers.mongo_crud import get_record_from_collection, insert_record_to_collection, update_record_in_collection, delete_record_from_collection, get_collections_from_db
from app.utils.constants import COLLECTION_NAMES, MESSAGE, RECORDS, USER, INSERT_MANY, FIND_MANY, DELETE_MANY
from app.utils.validators import ViewRecordRequest, InsertRecordRequest
from app.utils.utils import add_uuid_to_records
from app.utils.queries import generate_query

# crud_router = APIRouter(dependencies=[Depends(is_token_valid)])
crud_router = APIRouter()


@crud_router.get("/collections")
async def get_collections():
    collections = get_collections_from_db()
    collections.remove(USER)
    response = {
        COLLECTION_NAMES: collections,
        MESSAGE: "Collection Names Retrieved From The Data Base Successfully"
    }
    return JSONResponse(content=response)


@crud_router.get("/records/{collection_name}")
async def get_records(payload: ViewRecordRequest = Depends()):
    query = generate_query(payload.dict(exclude_none=True))
    records = get_record_from_collection(
        payload.collection_name, query=query, function=FIND_MANY)
    response = {
        RECORDS: records,
        MESSAGE: "Record(s) Retrieved From The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.post("/records")
async def insert_records(payload: InsertRecordRequest):
    payload.fields = add_uuid_to_records(payload.dict().get("fields"))
    record = insert_record_to_collection(
        **payload.dict(), function=INSERT_MANY)
    response = {
        MESSAGE: "Records Inserted to The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.delete("/records")
async def delete_record(payload: ViewRecordRequest):
    query = generate_query(payload.dict(exclude_none=True))
    records = delete_record_from_collection(
        payload.collection_name, query, DELETE_MANY)
    response = {
        # "deleted_record": record,
        MESSAGE: "Records Deleted From The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.get("/record/{collection_name}")
async def get_record(payload: ViewRecordRequest = Depends()):
    query = generate_query(payload.dict(exclude_none=True))
    records = get_record_from_collection(payload.collection_name, query=query)
    response = {
        RECORDS: [records],
        MESSAGE: "Record(s) Retrieved From The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.post("/record")
async def insert_record(payload: InsertRecordRequest):
    record = insert_record_to_collection(**payload.dict())
    response = {
        MESSAGE: "Record Inserted to The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.put("/record")
async def update_record(request: Request):
    payload = await request.json()
    record = update_record_in_collection(**payload)
    response = {
        MESSAGE: "Record Updated To The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.delete("/record")
async def delete_record(payload: ViewRecordRequest):
    query = generate_query(payload.dict(exclude_none=True))
    records = delete_record_from_collection(payload.collection_name, query)
    response = {
        # "deleted_record": record,
        MESSAGE: "Record Deleted From The Collection Successfully"
    }
    return JSONResponse(content=response)
