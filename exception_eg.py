import math
print(math.pi)
print(math.sqrt(25))
print(math.pow(5,2))
print(math.sin(90))
print(math.factorial(3))

# Exception hadling
try:
    num1= int(input("Enter a number:"))
    num2= int(input("Enter a number:"))
    print(num1/num2)
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as ex:
    print(f"Error: {ex}")

finally:
    print("called")

#math module
