from fastapi import FastAPI
from pydantic import BaseModel, Json
import uvicorn

app = FastAPI(title="Simple Containerized (Docker) FastAPI web app", version=1.0)


class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool


@app.get("/")
async def read_root():
    return {"data": "Hello this is a simple containerized FastAPI web app"}

@app.get("/health")
async def health_check():
    return {"status": "Helthy"}


@app.get("/items/{item_id}")
async def get_item(item_id):
    item = Item(id=item_id, name=f"Item{item_id}", is_offer=True, price=200)
    return {"data": item.model_dump()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
