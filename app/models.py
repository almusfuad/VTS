from pydantic import BaseModel
from datetime import date


class User(BaseModel):
      id: int
      name: str
      phone: str
      email: str
      password: str
      
class Movie(BaseModel):
      id: int
      name: str
      genre: str
      release_date: date

class Rating(BaseModel):
      id: int
      user_id: int
      movie_id: int
      rating: float