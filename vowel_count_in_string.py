#Count vowels in a string
vowel_list=[]
count=0
vowel=['a','e','i','o','u']
string = input("Enter the string:")
string_lower=string.lower()
#print(string_lower)
for i in string_lower:
    #print (i)
    for j in vowel:
        if (i==j):
            vowel_list.append(i)
            count+=1
print(f"vowels in the given string are {vowel_list}")
print(f"Vowels count={count}")