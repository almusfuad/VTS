import mysql.connector

# Establish connection to the Database
mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "",
      database = "movie_rating"
)

db_cursor = mydb.cursor()


def execute_query(query, values = None):
      db_cursor.execute(query, values)
      db_connection.commit()
      return db_cursor.fetchall()