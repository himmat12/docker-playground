from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import List

app = FastAPI(title="Simple Containerized (Docker) FastAPI web app", version=1.0)


class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool


# items collection list
items: List[Item] = []


@app.get("/")
async def read_root():
    return {"data": "Hello this is a simple containerized FastAPI web app"}


@app.get("/health")
async def health_check():
    return {"status": "Helthy"}


@app.get("/items/{id}")
async def get_item(id: int):
    error_msg = "Data not exists"
    item = next((item for item in items if item.id == id), error_msg)

    return {"data": item}


@app.get("/items")
async def get_items():
    return {"data": items}


@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return {
        "message": "successfully created item",
        "data": item,
        "count": len(items),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
