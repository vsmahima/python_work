def number_generator():
    for i in range(1,11):
        print(i)
        yield
a=number_generator()
for i in range(1,11):
    next(a)
    print("iteration incremented")