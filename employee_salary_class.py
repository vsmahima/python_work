#Store employee name and salary using constructor
# Display  the salary details

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        pass
    def print_salary(self):
        print("Employee Details")
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")
employee_name=input("Enter Employee Name: ")
employee_salary=int(input("Enter Employee Salary: "))
emp_obj = Employee(employee_name,employee_salary)
emp_obj.print_salary()
