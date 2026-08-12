def even_count(values):
    even=[]
    for i in values:
        if(i%2==0):
            even.append(i)
    length=len(even)
    # print(even,length)
    return length,even

values=[]
limit=int(input("Enter limit:"))
for i in range(1,(limit+1)):
    item=int(input(f"Enter {i} element:"))
    values.append(item)
[len,even_list]=even_count(values)
print(f"Even numbers in the list are: {even_list}")
print(f"Number of even number in the list is: {len}")