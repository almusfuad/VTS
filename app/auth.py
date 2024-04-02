from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
      return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
      verification_result = pwd_context.verify(plain_password, hashed_password)
      print("Verification Result:", verification_result)
      return verification_result