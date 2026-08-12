#simple calculator

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
op = input("Enter the operator:")
if(op=="+"):
    print(f"{num1}+{num2}={num1+num2}")
elif(op=="-"):
     print(f"{num1}-{num2}={num1-num2}")
elif(op=="*"):
    print(f"{num1}*{num2}={num1*num2}")
elif(op=="/"):
    print(f"{num1}/{num2}={num1/num2}")
else:
    print("Invalid operator")
