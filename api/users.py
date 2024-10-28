from fastapi import APIRouter, Depends, HTTPException
from Models.user import User

users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.get("/")
def get_users():
    return {"user":"Ravi"}

@users_router.post("/")
def create_user(user: User):
    return user

@users_router.get("/{user_id}")
def get_user(user_id: int):
    if user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id":user_id , "name":"Bhavya"}

@users_router.put("/{user_id}")
def create_user(user_id: int):
    return {"id":user_id , "name":"Bhavya Sri"}

@users_router.delete("/{user_id}")
def create_user(user_id: int):
    return {"msg":"user deleted successfully"}

# ... other user-related endpoints