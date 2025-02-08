from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import Settings


SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL

print("Database URL: ", SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)