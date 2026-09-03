import mysql.connector
#Create connection
conn=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="students"
)
#create cursor
cursor=conn.cursor()
# query="""
#     CREATE TABLE IF NOT EXIST student_info(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(50),
#     age INT,
#     department VARCHAR(50)
#     )
# """
#cursor.execute(query)
query="""
    INSERT INTO student_info(name,age,department) VALUES
    ("Manu",26,"DS"),
    ("Cathe",23,"IT")
"""
cursor.execute(query)
conn.commit()
conn.close()