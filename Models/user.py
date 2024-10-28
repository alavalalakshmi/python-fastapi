from fastapi import FastAPI,Body,Response
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    def _init_(self):
        id = 10
        name = "Bhavya"