from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.db import create_db_and_tbls
from app.core.config import settings
from app.api.routes import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    create_db_and_tbls()
    yield
    # shutdown


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

# include routers
app.include_router(users.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": f"Welome to {settings.PROJECT_NAME}"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
