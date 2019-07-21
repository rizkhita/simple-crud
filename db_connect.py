import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd=""
)

if db.is_connected():
    print("I am connected :D")
else :
    print("You failed to connect me :(")
