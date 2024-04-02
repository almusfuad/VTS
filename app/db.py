import mysql.connector

# Establish connection to the Database
mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "",
      database = "movie_rating"
)

db_cursor = mydb.cursor()

def execute_query(query, values=None, commit=False):
      try:
            db_cursor.execute(query, values)
            if commit:
                  mydb.commit()
            else:
                  db_cursor.fetchall()
      except mysql.connector.Error as e:
            print("Error executing query:", e)
            raise