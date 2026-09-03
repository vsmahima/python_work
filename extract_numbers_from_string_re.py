#extract all numbers from the string
import re
string = input("Enter the string: ")
print(string)
pattern = re.compile(r"\d+")
result = pattern.findall(string)
print(f"Digits in the string are: {result}")