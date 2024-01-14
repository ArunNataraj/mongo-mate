import datetime
import jwt
from fastapi import Request, HTTPException, status
from passlib.hash import pbkdf2_sha256
from app.utils.constants import EXP, EXP_MINS, AUTHORIZATION, SPACE, INVALID_EXPIRED_TOKEN, ACCESS_TOKEN_MISSING
from app.utils.config import ALGORITHM, TOKEN_SECRET_KEY


def generate_hash_password(password: str):
    hash = pbkdf2_sha256.hash(password)
    return hash


def verify_password(user_password: str, password:str):
    verify = pbkdf2_sha256.verify(password, user_password)
    return verify

def generate_access_token(payload: dict):
    token_expire_time = datetime.datetime.utcnow(
    ) + datetime.timedelta(minutes=EXP_MINS)
    to_encode = payload.copy()
    to_encode.update({EXP: token_expire_time})

    encoded_jwt = jwt.encode(to_encode, TOKEN_SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def is_token_valid(request: Request):
    try:
        authorization = request.headers.get(AUTHORIZATION)
        if authorization:
            access_token = authorization.split(SPACE)[1]
            jwt.decode(access_token, TOKEN_SECRET_KEY, algorithms=[ALGORITHM])
            return True
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=INVALID_EXPIRED_TOKEN
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ACCESS_TOKEN_MISSING
        )
