# String generator-a generator that takes a string and yield each cahr one by one.

def string_generator(str):
    for i in str:
        print (i)
        yield

str=input("Enter the string:")
a=string_generator(str)
for i in str:
    next(a)
