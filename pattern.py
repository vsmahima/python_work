import re
str="aaaabbccddffrreeddjhkjj"
patt=re.compile("ab*")
print(re.findall(patt,str))
patt=re.compile("ab+")
print(re.findall(patt,str))
patt=re.compile("ab?")
print(re.findall(patt,str))
print("Making non greedy")
patt=re.compile("ab*?")
print(re.findall(patt,str))
patt=re.compile("ab+?")
print(re.findall(patt,str))
patt=re.compile("ab??")
print(re.findall(patt,str))
# patt=re.compile("a*")
# patt=re.compile("a*")

# print(re.)