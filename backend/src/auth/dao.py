from src.dao import SQLAlchemyRepository
from src.auth.models import users, roles
from sqlalchemy import insert, select, update, delete, desc


class UsersDAO(SQLAlchemyRepository):
    model = users
    