from fastapi import FastAPI,Body,Response
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: int