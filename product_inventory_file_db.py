#product inventory-read product name quantity and price from a files and insert it into a sqlite product table
#calculate the total inventory value using the database records and save the report into inventory report.txt
#allow the user to add, update, delete and search product while keeping the file and database operation seperate
import csv
import sqlite3
class Database:
    def __init__(self):
        self.dbname="scope.db"
        self.conn=None
        self.cu=None
    def db_connection(self):
            try:
                self.conn=sqlite3.connect(self.dbname)
                self.cu=self.conn.cursor()
            except Exception as ex:
                print(f"Got Error: {ex}")
                        
    def db_table_creation(self):
        try:
            self.cu.execute("""CREATE TABLE IF NOT EXISTS product1 (pid INT PRIMARY KEY,
                product_name VARCHAR(50),category VARCHAR (50),price FLOAT(5,2),
                stock_quantity VARCHAR(50),supplier VARCHAR(50))""")
            with open("product_inventory.csv","r") as file:
                self.f=csv.reader(file)
                for row in self.f:
                    print(row)
                    self.cu.execute("""INSERT INTO product1 (pid,product_name,category,price,stock_quantity,supplier) 
                VALUES(?,?,?,?,?,?)""",row)
                    
        except Exception as ex:
                print(f"Got Error: {ex}")
                    
        self.conn.commit()
    def query(self,query,param): #for insert,update,delete from the user
            try:
                self.query=query
                self.param=param
                self.cu.execute(self.query,self.param)
                
            except Exception as ex:
                print(f"Got Error: {ex}")
            self.conn.commit()
    def db_close(self):
             self.cu.close()
             self.conn.close()
    def file_operation(self,*args):
         with open("product_inventory.csv","a+") as file:
            self.f=csv.writer(file)
            for i in args:
                 self.f.writerow(i)    
       
obj=Database()
obj.db_connection()
obj.db_table_creation()
print("""
    1.INSERT
    2.UPDATE
    3.DELETE
    4.CALCULATE INVENTORY COST
    5.EXIT
     """)
while True:
    choice=int(input("Enter your choice:"))
    if (choice==1):
        pid=int(input("Enter the product ID: "))
        pname=input("Enter the product name: ")
        cat=input("Enter the category: ")
        price=float(input("Enter price: "))
        squantity=int(input("Enter stock quantity: "))
        supplier=input("Enter supplier: ")
        query="""INSERT INTO product1 (pid,product_name,category,price,stock_quantity,supplier) 
          VALUES(?,?,?,?,?,?)"""
        obj.query(query,(pid,pname,cat,price,squantity,supplier))
        obj.file_operation((pid,pname,cat,price,squantity,supplier))
    elif(choice==2):
        pid=input("Enter the product ID: ")
        value=input("Enter the new value to update: ")
        query="""UPDATE employee1 set department=? WHERE emp_id=?"""
        obj.query(query,(value,emp_id))



