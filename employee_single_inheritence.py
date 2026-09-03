#Create a single inheritence employee Management system.
#employee store employee details and salary calculate monthly salary

class Employee:
    def __init__(self,name,id,dept,basic_pay):
        self.name=name
        self.id=id
        self.dept=dept
        self.basic_pay=basic_pay
    def display(self):
        print(f"Employee ID: {self.id}")
        print(f"Name of the Employee: {self.name}")
        print(f"Department: {self.dept}")
class Salary(Employee):
    def __init__(self,name,id,dept,basic_pay):
        super().__init__(name,id,dept,basic_pay)
        self.hra=0.30
        self.da=0.40
        self.net_salary=self.basic_pay+(self.hra*self.basic_pay)+(self.da*self.basic_pay)
    def display(self):
        super().display()
        print(f"Net salary: {self.net_salary}")
    
name= input("Emter Employee Name: ")
empid=int(input("Enter Employee Id: "))
dept=input("Enter department: ")
basic_pay=int(input("Enter Basic Pay: "))
obj=Salary(name,empid,dept,basic_pay)
obj.display()