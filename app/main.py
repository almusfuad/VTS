from fastapi import FastAPI
from routes import user_router, movie_router


app = FastAPI()

app.include_router(user_router)
app.include_router(movie_router)

if __name__ == "__main__":
      import uvicorn
      from db import mydb
      
      uvicorn.run(app, host="http://127.0.0.1/", port=8000)