from fastapi import APIRouter, Depends, HTTPException
from Models.product import Product

products_router = APIRouter(prefix="/products", tags=["Products"])

@products_router.get("/")
def get_products():
    return [{"id":12,"name":"ice cream", "price":200}]

@products_router.post("/")
def create_product(product: Product):
    return {"product created successfully"}

@products_router.get("/{product_id}")
def get_product(product_id: int):
    if product_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return [{"id":product_id,"name":"ice cream", "price":200}]

@products_router.put("/{product_id}")
def update_product(product: Product):
    return {"msg":"product updated successfully"}

@products_router.delete("/{product_id}")
def delete_product(product_id: int):
    return {"msg":"product deleted successfully"}
