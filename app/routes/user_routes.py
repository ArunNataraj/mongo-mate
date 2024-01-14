from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from app.utils.validators import UserRegistration
from app.helpers.token_manager import generate_hash_password
from app.helpers.user import create_user
from app.utils.constants import MESSAGE

user_router = APIRouter()


@user_router.post("/register")
async def user_registration(payload: UserRegistration):
    payload.password = generate_hash_password(payload.password)
    record = create_user(payload)
    response = {
        MESSAGE: "User Registered in Successfully"
    }
    return JSONResponse(content=response)
