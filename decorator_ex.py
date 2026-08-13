def hello(func):
    def sample(name):
        print("Welcome to scope india")
        func(name)
        print("ok,bye")
    return sample

@hello

def hi(name):
    print(f"This is {name}")

name=input("Enter the name: ")
hi(name)
