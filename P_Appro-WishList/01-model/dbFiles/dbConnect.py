import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(host="localhost:6060",
                                user="root",
                                password ="root",
                                database="WishList")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Wrong credentials..")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database doesn't exist...")
  else:
    print(err)
else:
  cnx.close()
  