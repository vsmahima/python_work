#Employee management-read employee details from a CSV file and insert the data into an SQLite employee table
#Allow the user to serach an employee by ID and save the search result into  a text file
#Update and delete employee records in the database and maintain a log file containing all opertations
import csv
import sqlite3
try:
    with open("employee.csv","r") as file:
        f=csv.reader(file)
        # for i in f:
        #     print(i)
    #inserting data to  the table employee
        conn=sqlite3.connect("scope.db")
        cu=conn.cursor()
        # cu.execute("""CREATE TABLE IF NOT EXISTS employee (emp_id INT PRIMARY KEY,
        #                            name VARCHAR(50),department VARCHAR(50))""")
        # for row in f:
        #     cu.execute("""INSERT INTO employee (emp_id,name,department) VALUES (?,?,?)""",row)
    #fetching info by id and store into taxt file
        print("Display content form the table employee")
        cu.execute("""SELECT * FROM employee WHERE emp_id=113 """)
        fe=cu.fetchall()
        for row in fe:
            print(fe)
    #writing content to the text file employee_info.txt
        f=open("employee_info.txt","w")
        for row in fe:
            f.write(str(row))
        conn.commit()
        conn.close()
except Exception as ex:
    print(f"Got Error: {ex}")
finally:
    print("Done")
