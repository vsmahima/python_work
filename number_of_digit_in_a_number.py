#single digit, double digit or more



num = int(input("Enter a number:"))
if(num<10):
    print(f"The given number {num} is single digit")
elif(num>=10 and num<100):
    print(f"The given number {num} is double digit")
else:
    print(f"The given number {num} has more than 2 digits")
    