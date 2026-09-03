import sqlite3
conn=sqlite3.connect("scope.db")
cu=conn.cursor()
cu.execute("""CREATE TABLE IF NOT EXISTS students(
                    name VARCHAR(30),
                    age INT)

            """)
# cu.execute("""INSERT INTO students(name,age) VALUES(?,?)""",("Manikarnika",3))
# value=[
#     ("Dua",4),
#     ("Harshig",3),
#     ("Ameya",3)
# ]
# cu.executemany("""INSERT INTO students(name,age) VALUES(?,?)""",value)
cu.execute("""SELECT * FROM students""")
fe=cu.fetchall()
for i in fe:
    print(i)
conn.commit()
conn.close()