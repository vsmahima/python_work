# Sum of digit in a number using for loop
num = int(input("Enter the number:"))
sum=0
for i in str(num):
    print(i)
    sum+=int(i)
print(f"Sum of digit= {sum}")
