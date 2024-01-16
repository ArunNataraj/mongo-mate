"""Authentication Routes"""
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.helpers.token_manager import is_token_valid
from app.helpers.user import verify_user
from app.utils.validators import UserRegistration
from app.utils.constants import MESSAGE, ACCESS_TOKEN, USER_LOGIN_MSG, USER_LOGOUT_MSG

session_router = APIRouter()


@session_router.post("/login")
async def login(payload: UserRegistration):
    """Login Endpoint"""
    access_token = verify_user(payload)

    response = {
        ACCESS_TOKEN: access_token,
        MESSAGE: USER_LOGIN_MSG
    }
    return JSONResponse(content=response)


@session_router.delete("/logout", dependencies=[Depends(is_token_valid)])
async def logout():
    """Logout Endpoint"""
    return USER_LOGOUT_MSG
