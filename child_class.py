from Student import Student 
class Child(Student):
    def __init__(self):
        super().__init__()
        print("Child class created")
    def grade(self):
        print("Grade Awarded:")
        if(self.avg>=80):
            print("A Grade")
        elif(self.avg>=60):
            print("B Grade")
        elif(self.avg>=40):
            print("C Grade")
        else:
            print("Faiiled")
    def __del__(self):
        print("Destructed")
obj=Child()
obj.get_input()
obj.display()
obj.total_marks()
obj.average()
obj.grade()
