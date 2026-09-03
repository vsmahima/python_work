#Student Records: Create a python program that reads student details from a text file and stores them in 
#SqLite students table.
#Display all student records from the databse and write the retrieved records into a output file.
#Handle file not found and database errors using appropriate exception handlinng
import csv
import sqlite3
try:
    with open("student.csv","r") as file:
        f=csv.reader(file)
        # for row in f:
        #     print(row)
        conn=sqlite3.connect("scope.db")
        cu=conn.cursor()
        # cu.execute("""CREATE TABLE student_info (name VARCHAR(50),age INT)
        #      """)
        #cu.execute("""DELETE FROM student_info WHERE name='Malhar'""")
        # cu.execute("""DROP TABLE student_info""")
        # for row in f:
        #     print(row)
        #     cu.execute("""INSERT INTO student_info(name,age) VALUES(?,?)""",row)
        ###Display content fromthe table###
        print("Display content from the table")
        cu.execute("""SELECT * FROM student_info""")
        fe=cu.fetchall()
        for row in fe:
            print(row)
        #Writing content to the text file student_info.csv
    with open("Student_info.csv","w") as file1:
        f1=csv.writer(file1)
        for row in fe:
            f1.writerow(row)


        conn.commit()
        conn.close()
        
except Exception as ex:
    print(f"Got Error: {ex}")
finally:
    print("Done.")
