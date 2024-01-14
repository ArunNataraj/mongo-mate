from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from app.helpers.token_manager import generate_access_token, is_token_valid
from app.helpers.user import verify_user
from app.utils.validators import UserRegistration

session_router = APIRouter()


@session_router.post("/login")
async def login(payload: UserRegistration):
    access_token = verify_user(payload)
   
    response = {
        "access_token": access_token,
        "message": "User Logged in Successfully"
    }
    return JSONResponse(content=response)


@session_router.delete("/logout", dependencies=[Depends(is_token_valid)])
async def logout(request: Request):
    return "logged out"
