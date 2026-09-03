def sum(*args):
    a=0
    for i in args:
        a+=i
    print(a)
sum()
sum(1,2)
sum(1,2,3)


#keywird argument example
def hello(**kwargs):
    print(kwargs)
hello(a=1,b=2)
hello(a=1,b=2,c=3)