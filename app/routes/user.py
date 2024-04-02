from fastapi import APIRouter, HTTPException, Depends
from db import execute_query
from auth import get_password_hash, verify_password
from models import User, LoginInput

user_router = APIRouter()


@user_router.post("/user/register/")
def register_user(user: User):
      hashed_password = get_password_hash(user.password)
      
      query = """  
            INSERT INTO users (name, phone, email, password)
            VALUES (%s, %s, %s, %s)
      """
      
      try:
            execute_query(query, (user.name, user.phone, user.email, hashed_password), True)
            return {'message': "User registered successfully"}
      except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to register user: {str(e)}")
      


@user_router.post("/user/login/")
def login_user(input_data: LoginInput):
      try:
            query = "SELECT password FROM movie_rating.users WHERE email = %s"
            result = execute_query(query, (input_data.email,))
            
            print(result)
            if not result:
                  raise HTTPException(status_code=401, detail="User not found")

            hashed_password = result[0][0]
            
            if not verify_password(input_data.password, hashed_password):
                  raise HTTPException(status_code=401, detail="Invalid email or password")
            
            return {'message': "Login successful"}
      except IndexError:
            raise HTTPException(status_code=401, detail="User not found")
      except HTTPException as http_exc:
            raise http_exc
      except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to login user: {str(e)}")