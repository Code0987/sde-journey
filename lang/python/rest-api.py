# python -m uvicorn rest-api:app --reload

import asyncio
import httpx
from fastapi import FastAPI, Query, HTTPException, Request, Depends
from pydantic import BaseModel


app = FastAPI()
app.items = {}


@app.get("/")
async def get():
    return {"message": "Welcome!"}


@app.get("/check")
async def get():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://httpbin.org/get")
            response.raise_for_status()
            res = response.json()
            return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


class Item(BaseModel):
    id: int | None = None
    name: str
    price: float


@app.get("/items/{item_id}", response_model=Item | None)
async def get_item(request: Request, item_id: int):
    print(request.headers)
    return app.items.get(item_id)


@app.post("/items/")
async def post_item(request: Request, item: Item, response_model=Item | None):
    print(request.headers)
    if item.id is None:
        item.id = len(app.items) + 1
    app.items[item.id] = item
    print(app.items)
    return item
