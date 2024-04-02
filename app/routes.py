from fastapi import APIRouter, HTTPException, Depends
from db import execute_post_query, execute_get_query
from auth import get_password_hash, verify_password, generate_access_token
from models import User, LoginInput, Movie, Rating
import mysql.connector

user_router = APIRouter()
movie_router = APIRouter()


@user_router.post("/user/register/")
def register_user(user: User):
      hashed_password = get_password_hash(user.password)
      
      query = """  
            INSERT INTO users (name, phone, email, password)
            VALUES (%s, %s, %s, %s)
      """
      
      try:
            execute_post_query(query, (user.name, user.phone, user.email, hashed_password))
            return {'message': "User registered successfully"}
      except mysql.connector.Error as e:
            raise HTTPException(status_code=500, detail=f"Failed to register user: {str(e)}")
      


@user_router.post("/user/login/")
def login_user(input_data: LoginInput):
      try:
            query = "SELECT password FROM movie_rating.users WHERE email = %s"
            result = execute_get_query(query, (input_data.email,))
            
            print(result)
            if not result:
                  raise HTTPException(status_code=401, detail="User not found")

            hashed_password = result[0][0]
            
            if not verify_password(input_data.password, hashed_password):
                  raise HTTPException(status_code=401, detail="Invalid email or password")
            
            
            access_token = generate_access_token(input_data.email)
            return {"access_token": access_token, "token_type": "bearer"}
      except IndexError:
            raise HTTPException(status_code=401, detail="User not found")
      except HTTPException as http_exc:
            raise http_exc
      except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to login user: {str(e)}")
      
      
@movie_router.post("/movie/")
def add_movie(movie: Movie):
      try:
            query = """
                  INSERT INTO movie_rating.movies (name, genre, rating, release_date)
                  VALUES (%s, %s, %s, %s)
             """
        
            execute_post_query(query, (
                  movie.name,
                  movie.genre,
                  movie.rating,
                  movie.release_date
            ))
        
            return {"message": "Movie added successfully"}
    
      except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to add movie: {str(e)}")
      
      
@movie_router.get("/movie/")
def get_movies():
      try:
            query = "SELECT * FROM movie_rating.movies"
            result = execute_get_query(query)
            
            movies = []
            for row in result:
                  movie = {
                        "id": row[0],
                        "name": row[1],
                        "genre": row[2],
                        "rating": row[3],
                        "release_date": row[4].strftime("%d-%m-%Y")
                  }
                  
                  movies.append(movie)
            
            return movies
           
      
      except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to get movies: {str(e)}")
      

