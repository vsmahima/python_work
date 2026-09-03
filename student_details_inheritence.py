class Student:
    def __init__(self,name,age):
        self.sname=name
        self.sage=age
    def display(self):
        print(f"Student Name: {self.sname}") 
        print(f"Student Age: {self.sage}")
class Child(Student):
    pass

name=input("Enter Name: ")
age=int(input("Enter age: "))
obj=Child(name,age)
obj.display()
        

        
