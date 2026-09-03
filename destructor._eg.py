class Number:
    def __init__(self,a,b):
        print("Called")
        self.a=a
        self.b=b
    def __del__(self):
        print("Destructed")
    def sum(self):
        print(f"sum={self.a+self.b}")
obj=Number(5,10)
obj.sum()