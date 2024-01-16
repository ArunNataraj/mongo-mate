"""User Methods"""
from fastapi import HTTPException, status
from app.helpers.mongo_orm import insert_record_to_collection, get_record_from_collection
from app.utils.constants import USER, EMAIL, INVALID_PASS, NOT_REGISTERED
from app.utils.utils import get_current_utc_time
from app.helpers.token_manager import generate_access_token, verify_password


def create_user(fields):
    """This Method Creates New User"""
    try:
        fields.created_at = get_current_utc_time()
        record = insert_record_to_collection(USER, fields.dict())
        return record
    except Exception as ex:
        print(ex)
        return ex


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
                detail=INVALID_PASS
            )

    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=NOT_REGISTERED
        )
