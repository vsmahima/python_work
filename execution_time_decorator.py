#Execution time decorator-Create a decorator that that prints function started before
#a function run and fuction stop after it finishes.

def decor(sum_digit):
    def execution_time(num1,num2):
        print("Function started...")
        sum_digit(num1,num2)
        print("Function Ended...")
    return execution_time

@decor
def sum(num1,num2):
    s=num1+num2
    print(f"Sum, {num1}+{num2}={s}")


num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
sum(num1,num2)
