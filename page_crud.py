import mysql.connector
import os

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="simple_crud")

def insert_data(db):
    name = input("name : ")
    address = input("address : ")
    val = (name,address)
    insert = db.cursor()
    insert_query = "INSERT INTO customers (name, address) VALUES (%s,%s)"
    insert.execute(insert_query,val)
    db.commit()
    print("{} data saved".format(insert.rowcount))

def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    results = cursor.fetchall()

    # if cursor.rowcount < 0:
    #     print("No Data Available")
    # else :
    for each_data in results :
        print("-----")
        print(each_data)

def update_data(db):
    cursor = db.cursor()
    cus_id = input("cutomer ID : ")
    name = input("name : ")
    address = input("address = ")
    sql = "UPDATE customers SET name=%s, address=%s WHERE cus_id=%s "
    val = (name, address, cus_id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data updated".format(cursor.rowcount))

def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    customer_id = input("pilih id customer> ")
    sql = "DELETE FROM customers WHERE customer_id=%s"
    val = (customer_id,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))



def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def show_menu(db):
    print("=== CRUD ?? ===")
    print("1. Insert ")
    print("2. Show")
    print("3. Update")
    print("4. Delete")
    print("5. Search")
    print("0. Out")
    print("------------------")
    menu = input("Choose code's menu : ")

    # clear screen
    os.system("clear")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while (True):
        show_menu(db)
