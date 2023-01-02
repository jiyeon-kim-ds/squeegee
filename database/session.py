from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{settings.mysql_username}:{settings.mysql_password}@{settings.mysql_server_name}:{settings.mysql_port}/{settings.mysql_database}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20,
    max_overflow=20,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
