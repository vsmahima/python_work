# String examples
f_name="manikarnika"
s_name="mahima"
print(f_name+s_name) #it will concatenate no spaces between word
print(f_name,s_name)#it will concatenate and add space between wrods
#convert to uppercase
print(f_name.upper())
print(s_name.upper())
#convert to lower case
print(f_name.lower())
print(s_name.lower())
#convert first letter into capital letter(title case)
print(f_name.title())
print(s_name.title())
#To remove special characters at position
name="@ mani@ka m@"
#remove special characters from the leftside
print(name.lstrip("@"))
#remove special characters at the leftside
print(name.rstrip("@"))
#remove special charachters form both side
print(name.strip("@"))
#----------SLICING-------------------
#print(f_name[3])
#print(f_name[3:])
#print(f_name[1:4])
#print(f_name[2:5])
print(f_name[-1])
print(f_name[-3])
print(f_name[-5])
print(f_name[::-1])
print(f_name[::-2])

#Exmple
num=5
#print(f_name+num)
print(f_name*num)
#format method example
num1=5
num2=6
print(f"first number={num1}, second number ={num2}, sum of 2 numbers {num1+num2}")
print(len(f_name))

