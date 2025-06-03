from fastapi import APIRouter, HTTPException
from starlette import status

from auth.schemas import UserRequest, TokenResponse
from auth.service import create_new_user, authenticate_user, create_access_token
from dependencies import db_dependency


router = APIRouter()


@router.post('/register', response_model=TokenResponse)
async def register_user(user_request: UserRequest, db: db_dependency):
    new_user = await create_new_user(user_request, db)
    token = create_access_token(new_user)
    return { 'access_token': token }


@router.post('/login', response_model=TokenResponse)
async def login_user(user_request: UserRequest, db: db_dependency):
    user = await authenticate_user(user_request, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Wrong username and password combination'
        )
    token = create_access_token(user)
    return token
