from fastapi import FastAPI,Query,Response
from Models.item import Item
from api.users import users_router
from api.products import products_router
app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")
def read_items(q: str = Query("hi", description="Query string"), page: int = Query(1, description="Page number")):
    return {"q": q, "page":page}

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    # Process the item data (e.g., save to a database)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    # Retrieve the existing item and update its properties
    return item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return Response(status_code=204)