import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="simple_crud")

cursor = db.cursor()

sql = "UPDATE customers SET name=%s, address=%s WHERE cus_id=%s"
val = ("Ardianta", "Lombok", 1)
cursor.execute(sql, val)

db.commit()

print("{} data updated".format(cursor.rowcount))
