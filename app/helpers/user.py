"""User Methods"""
from fastapi import HTTPException, status
from app.helpers.mongo_crud import insert_record_to_collection, get_record_from_collection
from app.utils.constants import USER, EMAIL
from app.utils.utils import get_current_utc_time
from app.helpers.token_manager import generate_access_token, verify_password


def create_user(fields):
    """This Method Creates New User"""
    fields.created_at = get_current_utc_time()
    record = insert_record_to_collection(USER, fields.dict())
    return record


def verify_user(fileds):
    """This Method Validates User And Generates Access Token"""
    query = {EMAIL: fileds.email}
    user = get_record_from_collection(USER, query)
    if user:
        if verify_password(user.get("password"), fileds.password):
            return generate_access_token(user)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Password"
            )

    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Not Registered / Invalid Email"
        )
