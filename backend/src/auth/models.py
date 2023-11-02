from src.database import Base
from sqlalchemy import Column, Integer, String, MetaData, Table


metadata = MetaData()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("fsd", String)
)