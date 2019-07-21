import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="simple_crud")

cursor = db.cursor()


sql = "SELECT * FROM customers"
cursor.execute(sql)

results = cursor.fetchall()
# results2 = cursor.fetchmany(2)
# results3 = cursor.fetchone()

for each_data in results:
    print(each_data)

print("-----")
# print(results3)
