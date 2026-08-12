#largest number in a list using for loop
limit=int(input("Enter the limit:"))
value=[]
i=1
while(i<=limit):
    var=int(input(f"Enter the {i} value:"))
    value.append(var)
    i+=1
print(value)
big=value[0]
for i in value:
    if(big<i):
        big=i
print(f"Largest number in the list is {big}")

