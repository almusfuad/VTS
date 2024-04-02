from fastapi import APIRouter, HTTPException, Depends
from db import execute_query
from auth import get_password_hash 
from models import User

user_router = APIRouter()


@user_router.post("/user/register/")
def register_user(user: User):
      hashed_password = get_password_hash(user.password)
      
      query = """  
            INSERT INTO users (name, phone, email, password)
            VALUES (%s, %s, %s, %s)
      """
      
      try:
            execute_query(query, (user.name, user.phone, user.email, hashed_password))
            return {'message': "User registered successfully"}
      except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to register user: {str(e)}")