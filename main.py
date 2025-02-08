from fastapi import FastAPI
from db.base_class import Base
from db.session import engine
from core.config import settings


def create_tables():
    Base.metadata.create_all(bind=engine)
    
    
def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
        )
    
    create_tables()
    return app

app = start_application()

@app.get("/")
def home():
    return {"msg":"Привет FastAPI🚀"}