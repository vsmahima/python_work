#create a class and objectfor thse student details
#display the student information
class Student:
    def __init__(self):
        print("Student Information")
        pass
    def get_student_info(self):
        self.sname=input("Enter Student Name: ")
        self.age=int(input("Enter Age: "))
        self.date_of_birth=input("Enter Date of birth: ")
        self.gender=input("Enter Gender: ")
        self.qualification=input("Enter Qualification: ")
    def print_student_info(self):
        print("Details are:")
        print(f"Student Name: {self.sname}")
        print(f"Date of Birth: {self.age}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Qualification: {self.qualification}")
stud_obj=Student()
stud_obj.get_student_info()
stud_obj.print_student_info()