import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="simple_crud")

cursor = db.cursor()

sql = "DELETE FROM customers WHERE cus_id=%s"
val = (3,)
cursor.execute(sql, val)

db.commit()

print("{} data dihapus".format(cursor.rowcount))
