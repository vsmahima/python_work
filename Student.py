class Student:
    def __init__(self):
        print("Parent class called...")
    def get_input(self):
        self.name=input("Enter Name: ")
        self.english=int(input("Enter marks scored for English: "))
        self.malayalam=int(input("Enter marks scored for Malayalam: "))
        self.science=int(input("Enter marks scored for Science: "))
        self.maths=int(input("Enter marks scored for Mathematics: "))
        self.it=int(input("Enter marks scored for IT: "))
    def display(self):
        print(f"Student Name: {self.name}")
        print("Subject and Marks")
        print(f"English: {self.english}")
        print(f"Malayalam: {self.malayalam}")
        print(f"Science: {self.science}")
        print(f"Mathematics: {self.maths}")
        print(f"IT: {self.it}")
    def total_marks(self):
        self.total=self.english+self.malayalam+self.science+self.maths+self.it
        print(f"Total Marks= {self.total}")
    def average(self):
        self.avg=self.total/5
        print(f"Average: {self.avg}")
# obj=Student()
# obj.get_input()
# obj.display()
# obj.total_marks()
# obj.average()

        
        
