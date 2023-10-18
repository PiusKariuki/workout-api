from fastapi import FastAPI
from sqlmodel import SQLModel
from .Routes import index_router
from .Core.config import settings
from .Database import engine
from fastapi.middleware.cors import CORSMiddleware


def include_router(application: FastAPI):
    application.include_router(index_router)


def create_tables():
    SQLModel.metadata.create_all(engine)


def start_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(application)
    return application


app = start_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
def home():
    return {"message": "success"}
