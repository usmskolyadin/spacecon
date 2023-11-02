from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str
    user_id: int

class User(BaseModel):
    username: str
    email: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str