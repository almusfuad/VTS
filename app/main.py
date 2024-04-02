from fastapi import FastAPI
from routes import user_router


app = FastAPI()

app.include_router(user_router)

if __name__ == "__main__":
      import uvicorn
      from db import mydb
      
      uvicorn.run(app, host="http://127.0.0.1/", port=8000)