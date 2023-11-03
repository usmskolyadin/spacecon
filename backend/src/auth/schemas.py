from datetime import datetime
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str
    user_id: int

class User(BaseModel):
    id: int
    email: str
    username: str
    registered_at: datetime


class UserAuth(BaseModel):
    id: int
    email: str
    username: str
    password: str
    registered_at: datetime

class UserInDB(User):
    password: str