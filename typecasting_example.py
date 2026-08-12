a=5
b=float(a)
print(b)
str=str(a)
print(str)
#list to tuple
lst=[1,2,3,4,5]
tp=tuple(lst)
print(tp)
# list to set
st=set(tp)
print(st)
# tuple to list
tp1=(11,22,33,44,55)
lst1=list(tp1)
print(lst1)
#tuple to set
st1=set(tp1)
print(st1)
# list to dictionary
values=[("Name",["Manikarnika","Malhar","Siva"]),
        ("Age",[3,1,1]),("Gender",["female","male","male"])]
dic_values=dict(values)
print(dic_values)
import pandas as pd
df=pd.DataFrame(dic_values)
print(df)