import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="simple_crud")

cursor = db.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
  ("Doni", "Jakarta"),
  ("Ella", "Surabaya"),
  ("Fani", "Bandung"),
  ("Galih", "Depok")
]

for val in values:
    cursor.execute(sql,val)
    db.commit()

print("{} many data added".format(len(values)))
