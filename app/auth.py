from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "36FF534EDD58DAAB1D7CE37996893"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 180

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
      return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
      verification_result = pwd_context.verify(plain_password, hashed_password)
      print("Verification Result:", verification_result)
      return verification_result

def generate_access_token(email):
      to_encode = {
            "sub": email,
            "exp": datetime.utcnow() + timedelta(
                  minutes=ACCESS_TOKEN_EXPIRE_MINUTES
            )
      }
      
      return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)