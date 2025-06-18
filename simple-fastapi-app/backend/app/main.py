from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.db import create_db_and_tbls
from core.config import settings
from api.routes import users

import uvicorn


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
    return {"message": f"Welome to {settings.PROJECT_NAME}. This is new update. V1.0 completed. Dockerfile updated - `CMD updated with sh script.`"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

 
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)