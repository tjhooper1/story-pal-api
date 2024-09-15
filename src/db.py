from sqlalchemy import create_engine

from models import Base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL
)
Base.metadata.create_all(bind=engine)