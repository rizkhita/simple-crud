import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="simple_crud")

cursor = db.cursor()

"""
name = "Dian"
address = "Mataram"
sql = "INSERT INTO customers (name, address) VALUES ('"+ name +"', '" + address +"')"
"""

sql ="INSERT INTO customers (name,address) VALUES (%s,%s)"
a="Kibi"
b="Batam"
val=(a,b)
cursor.execute(sql,val)

db.commit()
print("{} data added".format(cursor.rowcount))
