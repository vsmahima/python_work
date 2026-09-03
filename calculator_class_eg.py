class Calculator:
    def sum(self):
        num1=int(input("Enter first number: "))
        num2= int(input("Enter second number: "))
        print(f"{num1}+{num2}={num1+num2}")
    def sub(self):
        num1=int(input("Enter first number: "))
        num2= int(input("Enter second number: "))
        print(f"{num1}-{num2}={num1-num2}")


obj=Calculator()
obj.sum()
obj.sub()