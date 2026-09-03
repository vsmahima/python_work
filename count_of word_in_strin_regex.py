#Count how many times a word appear in a string
import re
string="The government announced a new education policy today. The education policy focuses on improving schools, and the new policy will provide better facilities for students. Schools will receive additional funding, and students will benefit from the improved education system."
print(string)
word=(input("Enter the word to find: "))
# pattern=re.compile(r"{word}")
result=re.findall(word,string,re.IGNORECASE)
print(result)
res_len=len(result)
print(f"The given word appear in {res_len} times")