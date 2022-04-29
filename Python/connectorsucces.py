import mysql.connector

db = mysql.connector.connect(host = "localhost",
                             user= "root",
                             password="23512351")

if db:
    print("connection is successful")
else:
    print("Connection is unsuccessful")
