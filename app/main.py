from fastapi import FastAPI
from routes.user import user_router
import uvicorn
from db import mydb


app = FastAPI()

app.include_router(user_router)

if __name__ == "__main__":
      
      
      uvicorn.run(app, host="http://127.0.0.1/", port=8000)