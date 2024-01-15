"""Authentication Routes"""
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from app.helpers.token_manager import is_token_valid
from app.helpers.user import verify_user
from app.utils.validators import UserRegistration
from app.utils.constants import MESSAGE

session_router = APIRouter()


@session_router.post("/login")
async def login(payload: UserRegistration):
    """Login Endpoint"""
    access_token = verify_user(payload)

    response = {
        "access_token": access_token,
        MESSAGE: "User Logged in Successfully"
    }
    return JSONResponse(content=response)


@session_router.delete("/logout", dependencies=[Depends(is_token_valid)])
async def logout(request: Request):
    """Logout Endpoint"""
    return "logged out"
