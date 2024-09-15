from fastapi import APIRouter, HTTPException

from auth import get_user_by_email
from models import User


router = APIRouter()

@router.post("/register")
async def register(user: User):
    return {"message": "User registered successfully"}

@router.post("/token")
async def get_token(user: User):
    return {"message": "User logged in successfully"}


@router.post("/login")
async def login(user: User):
    user = get_user_by_email(user.email)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    if not user.hashed_password:
        raise HTTPException(status_code=400, detail="User not found")
    return {"message": "User logged in successfully"}


@router.post("/logout")
async def logout(user: User):
    return {"message": "User logged out successfully"}

