from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text
from src.config import settings

engine = create_async_engine(
    settings.db.url,
    echo=settings.db.echo,
    pool_size=5,
    max_overflow=10
)

Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
