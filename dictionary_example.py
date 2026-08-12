#dictionary example
value_dict={"name":"Mahima","gender":"female"}
print(value_dict)
value_dict1={"name":["Manikarnika","Malhar","Siva"],"age":[3,1,1]}
print(value_dict1)
#add new column or key to existing dictionary
value_dict1["gender"]=['female','male','female']
print(value_dict1)
#print the ditionary in table format
import pandas as pd
df=pd.DataFrame(value_dict1)
print(df)
#to print the keys in the dictionary
print(value_dict1.keys())
#to print the values in the dictionary
print(value_dict1.values())
#print the values in th eparticular key or column
print(value_dict1["name"])
#to print the key and value together
print(value_dict1.items())
#to delete/remove the column/key
value_dict1.pop("gender")
print(value_dict1)


# #convert list to dictionary
# values=[[1,'a'],[2,'b'],[3,'c']]
# print(values)
# dict_values=dict(values)
# print(dict_values)
# print(type(dict_values))
# # program from the 