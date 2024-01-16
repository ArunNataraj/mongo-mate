"""User Routes"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils.validators import UserRegistration
from app.helpers.token_manager import generate_hash_password
from app.helpers.user import create_user
from app.utils.constants import MESSAGE, USER_REGISTRATION_MSG

user_router = APIRouter()


@user_router.post("/register")
async def user_registration(payload: UserRegistration):
    """User Registration Endpoint"""
    payload.password = generate_hash_password(payload.password)
    record = create_user(payload)
    response = {
        MESSAGE: USER_REGISTRATION_MSG
    }
    return JSONResponse(content=response)
