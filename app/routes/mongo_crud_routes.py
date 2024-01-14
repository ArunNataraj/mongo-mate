from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from app.helpers.token_manager import is_token_valid
from app.helpers.mongo_crud import get_records_from_collection, insert_record_to_collection, update_record_in_collection, delete_record_from_collection, get_collections_from_db
from app.utils.constants import COLLECTION_NAMES, MESSAGE, RECORDS, USER
from app.utils.validators import RecordRequest

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
async def get_records(payload: RecordRequest = Depends()):
    records = get_records_from_collection(**payload.dict(exclude_none=True))
    print(records)
    response = {
        RECORDS: records,
        MESSAGE: "Record(s) Retrieved From The Collection Successfully"
    }
    return JSONResponse(content=response)


@crud_router.get("/record")
async def get_record():
    return "GET method"


@crud_router.post("/record")
async def insert_record(request: Request):
    payload = await request.json()
    record = insert_record_to_collection(**payload)
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
async def delete_record(request: Request):
    payload = await request.json()
    record = delete_record_from_collection(**payload)
    response = {
        "deleted_record": record,
        MESSAGE: "Record Deleted From The Collection Successfully"
    }
    return JSONResponse(content=response)
