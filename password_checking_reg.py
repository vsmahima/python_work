#validate a password that contain atleast one uppercase,one lowercase,one digit and one special charecter
import re
password=input("Enter your password: ")
#pattern = re.compile(r"[\da-zA-Z@#$%?^&]+")
pat = re.compile(r"^(?=.*[a-z])$")
print(pat)
result=re.fullmatch(pat,password)
#print(result)
print(bool(result))
if(bool(result)==True):
    print("Succesfully created password")
else:
    print("Please check the password: ")
    print("Password should have atleast one Uppercase letter,\n atleast one lowercase letter,\n atleast one digit and \natleast one special characters @#$%?^&")