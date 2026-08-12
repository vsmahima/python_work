#Get number sgrater than 50 
def greaterthan50(values):
    val_50=[]
    for i in values:
        if(i>50):
            val_50.append(i)
    print(val_50)


values=[]
limit=int(input("Enter limit:"))
for i in range(1,(limit+1)):
    item=int(input(f"Enter {i} element:"))
    values.append(item)
print(values)
greaterthan50(values)