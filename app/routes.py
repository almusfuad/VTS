from fastapi import APIRouter, HTTPException, Depends, Path
from fastapi.responses import JSONResponse
from auth import get_password_hash, verify_password, generate_access_token
from models import User, LoginInput, Movie, Rating
import mysql.connector
from db import execute_post_query, execute_get_query

user_router = APIRouter()
movie_router = APIRouter()


@user_router.post("/user/register/", tags=["User"])
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
      


@user_router.post("/user/login/", tags=["User"])
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
      
      
@movie_router.post("/movie/", tags=["Movie"])
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
      
      
@movie_router.get("/movie/", tags=["Movie"])
def get_movies():
      try:
            query = """
                  SELECT m.id, m.name, m.genre, AVG(r.rating) as average_rating, m.release_date 
                  FROM movie_rating.movies m
                  JOIN movie_rating.ratings r ON m.id = r.movie_id
                  GROUP BY m.id, m.name, m.genre, m.release_date
            """
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
      



@movie_router.get("/movie/{movie_name}", tags=["Movie"])
def search_movie(movie_name: str = Path(..., title = "Movie Name", description="Name of the movie to search for")):
      try:
            query = """ 
                  SELECT m.id, m.name, m.genre, AVG(r.rating) as average_rating, m.release_date 
                  FROM movie_rating.movies m
                  JOIN movie_rating.ratings r ON m.id = r.movie_id
                  WHERE m.name LIKE %s
                  GROUP BY m.id, m.name, m.genre, m.release_date
            """ 
            
            result = execute_get_query(query, (f"%{movie_name}%", ))  # added % to enable partial match
            
            if not result:
                  raise HTTPException(status_code=404, detail="No movies found with the provided name")
            
            movies = []
            for row in result:
                  movie = {
                        "id": row[0],
                        "name": row[1],
                        "genre": row[2],
                        "average_rating": row[3],
                        "release_date": row[4].strftime("%d-%m-%Y")
                  }
                  
                  movies.append(movie)
            return movies
      except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to search for movies: {str(e)}")
                  
      


@movie_router.post("/rating/", tags=["Rating"])
def add_rating(rating: Rating):
      try:
            query = """
                  INSERT INTO movie_rating.ratings (user_id, movie_id, rating)
                  VALUES (%s, %s, %s)
            """
            
            execute_post_query(query, (rating.user_id, rating.movie_id, rating.rating))
            return {"message": "Rating added successfully"}
      except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to add rating: {str(e)}")
      


@movie_router.get("/rating/", tags=["Rating"])
def all_rating():
      try:
            query = '''
                  SELECT * FROM movie_rating.ratings
            '''
            result = execute_get_query(query)
            
            ratings = []
            for row in result:
                  rating = {
                        'id': row[0],
                        'user_id': row[1],
                        'movie_id': row[2],
                        'rating': row[3]
                  }
                  ratings.append(rating)
                  
            return ratings
      
      except Exception as e:
            return HTTPException(status_code=500, detail=f"Failed to get ratings: {str(e)}")
      
      
