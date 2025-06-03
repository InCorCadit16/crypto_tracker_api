from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from starlette import status

from auth.models import User
from auth.schemas import UserRequest
from config import settings

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


async def create_new_user(user_request: UserRequest, db: AsyncSession) -> User:
    user = User(
        username=user_request.username,
        password_hash=bcrypt_context.hash(user_request.password.get_secret_value())
    )
    db.add(user)
    try:
        await db.commit()
    except IntegrityError as ie:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This username already exists')

    await db.refresh(user)
    return user


async def authenticate_user(user_request: UserRequest, db: AsyncSession) -> Optional[User]:
    user = await get_user(db, username=user_request.username)
    if user and bcrypt_context.verify(user_request.password.get_secret_value(), user.password_hash):
        return user
    return None


def create_access_token(user: User):
    expires = datetime.now() + timedelta(seconds=settings.TOKEN_EXPIRATION_SECONDS)
    encode = {
        'sub': user.username,
        'id': user.id,
        'exp': expires
    }
    return jwt.encode(encode, settings.AUTH_SECRET_KEY, algorithm='HS256')


async def get_current_user(token: str, db: AsyncSession) -> User:
    try:
        payload = jwt.decode(token, settings.AUTH_SECRET_KEY, algorithms=['HS256'])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        print(f'user id is {user_id}')
        if not username or not user_id:
            raise JWTError

        user = await get_user(db, user_id=user_id)
        if not user or user.username != username:
            raise JWTError

        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user'
        )


async def get_user(db: AsyncSession, user_id: int = None, username: str = None) -> Optional[User]:
    result = None
    if user_id:
        result = await db.execute(select(User).where(User.id == user_id))
    elif username:
        result = await db.execute(select(User).where(User.username == username))

    return result.scalar_one_or_none() if result else None
