values=[11,22,33,55.0,"mani",True]
print(values)
print(type(values))
#update values in list
values[0]=111
print(values)
#add new value to a list - append
values.append(222)
print(values)
#adding new value in the particular position-insert
values.insert(3,47)
print(values)
#remove/delete value from the list given value
values.remove(47)
print(values)
#remove values based on index
values.pop(5)
print("After removing")
print(values)
#---------slicing------
print(values[2])
print(values[2:])
print(len(values))
