#Largest number in the list
def largest(values):
    print(values)
    big=values[0]
    for i in values:
        if(big<i):
            big=i
    return big


values=[]
limit=int(input("Enter limit:"))
for i in range(1,(limit+1)):
    item=int(input(f"Enter {i} element:"))
    values.append(item)
#print(values)
b=largest(values)
print(f"Biggest element in the list = {b}")