# Larger number using lambda

large = lambda num1,num2: num1 if(num1>num2)  else num2
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(f"Largest number is:{large(num1,num2)}")    