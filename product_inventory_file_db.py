#product inventory-read product name quantity and price from a files and insert it into a sqlite product table
#calculate the total inventory value using the database records and save the report into inventory report.txt
#allow the user to add, update, delete and search product while keeping the file and database operation seperate
import csv
import sqlite3
try:
    conn=sqlite3.connect("scope.db")
    cu=conn.cursor()
    with open("product_inventory.csv","a+") as file:
        f=csv.reader(file)
        # for line in f:
        #     print(line)
    # cu.execute("""CREATE TABLE IF NOT EXISTS product (pid INT PRIMARY KEY,
    # product_name VARCHAR(50),category VARCHAR (50),price FLOAT(5,2),
    # stock_quantity VARCHAR(50),supplier VARCHAR(50))""")
        # for row in f:
        #     cu.execute("""INSERT INTO product (pid,product_name,category,price,stock_quantity,supplier) 
        #     VALUES(?,?,?,?,?,?)""",row)
    f=open("inventory_report.txt","a+")
    cu.execute("""SELECT product_name,price from PRODUCT""")
    fe=cu.fetchall()
    for row in fe:
        f.write(str(row))
    conn.commit()
    conn.close()
except Exception as ex:
    print(f"Got error: {ex}")
finally:
    print("Done")


