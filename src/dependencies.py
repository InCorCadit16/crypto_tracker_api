from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends
from auth.models import User
from auth.service import get_current_user, oauth2_bearer
from database import get_db_session

db_dependency = Annotated[AsyncSession, Depends(get_db_session)]

async def user_dependency(token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency):
    return await get_current_user(token, db)


auth_dependency = Annotated[User, Depends(user_dependency)]
