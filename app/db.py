import mysql.connector

# Establish connection to the Database
mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "",
      database = "movie_rating"
)

db_cursor = mydb.cursor()

def execute_post_query(query, values=None):
      try:
            db_cursor.execute(query, values)
            mydb.commit()
      except mysql.connector.Error as e:
            print("Error executing query:", e)
            raise

def execute_get_query(query, values=None):
      try:
            db_cursor.execute(query, values)
            return db_cursor.fetchall()
      except mysql.connector.Error as e:
            print("Error executing GET query:", e)
            raise