#Employee management-read employee details from a CSV file and insert the data into an SQLite employee table
#Allow the user to serach an employee by ID and save the search result into  a text file
#Update and delete employee records in the database and maintain a log file containing all opertations
import csv
import sqlite3
import datetime
class Database:
    def __init__(self):
        self.dbname="scope.db"
        self.conn=None
        self.cu=None
        self.time=datetime.datetime.now().strftime("%y:%m:%d %H:%M:%S")
    def log_maintain(self,log_date,db_details):
        with open("dblog.txt","+a") as file:
            file.write(f"{log_date}:{db_details}\n")
    def db_connection(self):
        try:
            self.conn=sqlite3.connect(self.dbname)
            self.cu=self.conn.cursor()
            self.msg="Database connected successfully"+str(self.conn)
            self.log_maintain(self.time,self.msg)
        except Exception as ex:
                    print(f"Got Error: {ex}")
                    self.log_maintain(self.time,ex)
    def db_table_creation(self):
        try:
            self.cu.execute("""CREATE TABLE IF NOT EXISTS employee1 (emp_id INT PRIMARY KEY,
                                    name VARCHAR(50),department VARCHAR(50))""")
            self.msg="Table crated"+str(self.cu.execute)
            self.log_maintain(self.time,self.msg)
            ##filling table value from the file for the first time
            with open("employee.csv","r") as file:
                f=csv.reader(file)
                for row in f:
                    self.cu.execute("""INSERT INTO employee1 (emp_id,name,department) VALUES (?,?,?)""",row)
            self.msg="Data from the file inserted succsefully"
            self.log_maintain(self.time,self.msg)
        except Exception as ex:
            print(f"Got Error: {ex}")
            self.log_maintain(self.time,ex)
        self.conn.commit()
    def query(self,query,param): #for insert,update,delete from the user
        try:
            self.query=query
            self.param=param
            self.cu.execute(self.query,self.param)
            self.msg="Database activity insert/update/delete done succefully"
            self.log_maintain(self.time,self.msg)
        except Exception as ex:
            print(f"Got Error: {ex}")
            self.log_maintain(self.time,ex)
        self.conn.commit()
    def select_query(self,query,param):
        try:
            self.query=query
            self.param=param
            self.cu.execute(self.query,self.param)
            self.fe=self.cu.fetchall()
            print(f"Details of the employee with id {self.param}")
            f=open("employee_info.txt","a+")
            for row in self.fe:
                print(self.fe)
            #writing content to the file
                f.write(str(row),'\n')

        except Exception as ex:
            print(f"Got Error: {ex}")
            self.log_maintain(self.time,ex)
        self.conn.commit()
    def db_close(self):
         self.cu.close()
         self.conn.close()
    
obj=Database()
obj.db_connection()
#obj.db_table_creation()
print("""
    1.INSERT
    2.UPDATE
    3.DELETE
    4.SELECT
    5.EXIT
     """)
###USER interaction with the database
while True:
    choice=int(input("Enter your choice:"))
    if (choice==1):
        emp_id=int(input("Enter the employee ID: "))
        name=input("Enter the name of the employee: ")
        department=input("Enter the department: ")
        query="""INSERT INTO employee1 (emp_id,name,department) VALUES (?,?,?)"""
        obj.query(query,(emp_id,name,department))
    elif(choice==2):
        emp_id=input("Enter the id of the employee to update: ")
        value=input("Enter the new value to update: ")
        query="""UPDATE employee1 set department=? WHERE emp_id=?"""
        obj.query(query,(value,emp_id))
    elif(choice==3):
        emp_id=input("Enter the id of the employee to delete: ")
        del_query="""DELETE FROM employee1 WHERE emp_id=?"""
        obj.query(del_query,(emp_id,))
    elif(choice==4):
        print("Fetching the output from the table and wtite it into a file")
        emp_id=input("Enter the id of the employee to search: ")
        sel_query="""SELECT * FROM employee WHERE emp_id=?"""
        obj.select_query(sel_query,(emp_id,))
    elif(choice==5):
        print("Exit from database activities")
        break
    else:
        print("Wrong choice, please check your input")
obj.db_close()
     
