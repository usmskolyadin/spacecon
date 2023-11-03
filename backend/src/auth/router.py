from src.auth.utils import get_hashed_password
from fastapi import APIRouter, Depends
from src.auth.schemas import User, UserAuth
from src.auth.dao import UsersDAO
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import async_session

auth = APIRouter()

@auth.post('/signup', summary="Create new user", response_model=UserAuth)
async def create_user(user_data: UserAuth, session: AsyncSession = Depends(async_session)):
    user = {
        "id": user_data.id,
        "email": user_data.email,
        "username": user_data.username,
        "password": get_hashed_password(user_data.password),
        "registered_at": user_data.registered_at,
    }
    return await UsersDAO(session).add_one(user)
