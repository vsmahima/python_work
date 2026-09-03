#Check whether a phone number is exactly 10 digit
import re
ph_num=input("Enter your phone number: ")
pattern = re.compile(r"[0-9]+")
result=re.fullmatch(pattern,ph_num)
#print(bool(result))
if(bool(result)==False):
    print("Please enter valid phone number")
else:
    length=len(ph_num)
    if(length<10):
        print("Phone number should have 10 digit")
    else:
        print("Valid number")