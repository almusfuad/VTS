import pytest
from main import app
from fastapi.testclient import TestClient
from routes import user_router, movie_router
from starlette.testclient import TestClient

user_client = TestClient(user_router)
movie_client = TestClient(movie_router)


def test_register_user():
      user_data = {
            "name": "John Doe",
            "phone": "1234567890",
            "email": "john@example.com",
            "password": "password123"
      }
      
      response = user_client.post("/user/register/", json=user_data)
      assert response.status_code == 200
      assert response.json() == {'message': "User registered successfully"}
      
def test_login_user():
      login_data = {
            "email": "john@example.com",
            "password": "password123"
      }
      
      response = user_client.post("/user/login/", json=login_data)
      assert response.status_code == 200
      assert "access_token" in response.json()
      assert "token_type" in response.json()
 
 
      
def test_add_movie():
      movie_data = {
            "name": "Inception",
            "genre": "Science Fiction",
            "rating": "PG-13",
            "release_date": "2010-07-16"
      }
      
      response = movie_client.post("/movie/", json=movie_data)
      assert response.status_code == 200
      assert response.json() == {'message': "Movie added successfully"}
      

def test_get_movies():
      response = movie_client.get("/movie/")
      assert response.status_code == 200
      assert isinstance(response.json(), list)
      assert len(response.json()) > 0
      
def test_search_movie():
      response = movie_client.get("/movie/Inception")
      assert response.status_code == 200
      assert isinstance(response.json(), list)
      assert len(response.json()) > 0

def test_add_rating():
      rating_data = {
            "user_id": 4,
            "movie_id": 3,
            "rating": 5.0
      }
      response = movie_client.post("/rating/", json=rating_data)
      assert response.status_code == 200
      assert response.json() == {'message': "Rating added successfully"}
      

import pytest
from fastapi.testclient import TestClient
from routes import user_router, movie_router
from starlette.testclient import TestClient

user_client = TestClient(user_router)
movie_client = TestClient(movie_router)


def test_register_user():
      user_data = {
            "name": "John Doe",
            "phone": "1234567890",
            "email": "john@example.com",
            "password": "password123"
      }
      
      response = user_client.post("/user/register/", json=user_data)
      assert response.status_code == 200
      assert response.json() == {'message': "User registered successfully"}
      
def test_login_user():
      login_data = {
            "email": "john@example.com",
            "password": "password123"
      }
      
      response = user_client.post("/user/login/", json=login_data)
      assert response.status_code == 200
      assert "access_token" in response.json()
      assert "token_type" in response.json()
 
 
      
def test_add_movie():
      movie_data = {
            "name": "Inception",
            "genre": "Science Fiction",
            "rating": "PG-13",
            "release_date": "2010-07-16"
      }
      
      response = movie_client.post("/movie/", json=movie_data)
      assert response.status_code == 200
      assert response.json() == {'message': "Movie added successfully"}
      

def test_get_movies():
      response = movie_client.get("/movie/")
      assert response.status_code == 200
      assert isinstance(response.json(), list)
      assert len(response.json()) > 0
      
def test_search_movie():
      response = movie_client.get("/movie/Inception")
      assert response.status_code == 200
      assert isinstance(response.json(), list)
      assert len(response.json()) > 0

def test_add_rating():
      rating_data = {
            "user_id": 4,
            "movie_id": 3,
            "rating": 5.0
      }
      response = movie_client.post("/rating/", json=rating_data)
      assert response.status_code == 200
      assert response.json() == {'message': "Rating added successfully"}
      

def test_all_rating():
      response = movie_client.get("/rating/")
      assert response.status_code == 200
      assert isinstance(response.json(), list)
      assert len(response.json()) >= 0