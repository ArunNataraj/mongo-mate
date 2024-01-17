"""Authentication Routes"""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from app.helpers.token_manager import is_token_valid, black_list_token
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
async def logout(request: Request):
    """Logout Endpoint"""
    black_list_token(request)
    response = {
        MESSAGE: USER_LOGOUT_MSG
    }
    return JSONResponse(content=response)
