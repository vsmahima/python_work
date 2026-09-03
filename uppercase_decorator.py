#upper case decorator_a decorator that converts returned string from  a function into upper case.


def decor(upper):
    def rec_fun(string):
        print(f"String before convertng into uppercase, {string}")
        print(f"String converted to uppercase.")
        upper(string)
        print("Suucess...")
    return rec_fun

@decor

def convert_upper(str):
    print(str.upper())

str=input("Enter the string:")
convert_upper(str)