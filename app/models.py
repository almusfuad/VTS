from pydantic import BaseModel
from datetime import date


class User(BaseModel):
      name: str
      phone: str
      email: str
      password: str
      
class LoginInput(BaseModel):
      email: str
      password: str
      
class Movie(BaseModel):
      name: str
      genre: str
      release_date: date

class Rating(BaseModel):
      user_id: int
      movie_id: int
      rating: float