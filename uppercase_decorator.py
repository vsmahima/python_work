def decor(upper):
    def rec_fun(string):
        print(f"String before convertng into uppercase, {string}")
        upper(string)
        print(f"String converted to uppercase.")
    return rec_fun

@decor

def convert_upper(str):
    print(str.upper())

str=input("Enter the string:")
convert_upper(str)