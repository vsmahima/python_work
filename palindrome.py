#check palindrome unsing for loop
string=input("Enter the string:")
str_lower=string.lower()
string_rev=str_lower[::-1]
length=len(string)
count=1
print(f"Reverse of the string = {string_rev}")
for i in range(0,length):
    if(str_lower[i]!=string_rev[i]):
        count=0
        break
if(count==0):
    print("The given string is not palindrome")
else:
    print("The given string is palindrome")
