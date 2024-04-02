import unittest
from fastapi.testclient import TestClient
from routes import user_router
import bcrypt

client = TestClient(user_router)

class TestUserRoutes(unittest.TestCase):
      def test_register_user(self):
            # Hash the password before sending the request
            hashed_password = bcrypt.hashpw("pass1".encode(), bcrypt.gensalt())
            
            user_data = {
                  "name": "John Doe",
                  "phone":"11111111111",
                  "password":hashed_password.decode(),
                  "email":"john_doe@gmail.com"
            }
            
            
            
            response = client.post("/user/register/", json=user_data)
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {'message': "User registered successfully"})
            
      
      def test_login_user(self):
            login_data = {
                  "email": "john_doe@gmail.com",
                  "password": "pass1"
            }
            
            # Encode the plain text password to bytes
            password_bytes = login_data["password"].encode()

            # Hash the plain text password using bcrypt
            hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

            # Update the login data with the hashed password
            login_data["password"] = hashed_password.decode()  # Convert bytes to string
            
            response = client.post("/user/login/", json=login_data)
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {'message': "Login successful"})
            
if __name__ == "__main__":
      unittest.main()