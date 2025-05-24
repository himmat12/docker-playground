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


@app.get("/items/{item_id}")
async def get_item(item_id):
    for item in items:
        filtered_items = filter(item.id == item_id, items)

    return {"data": filtered_items[0]}


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
