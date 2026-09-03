#NUmber generator: generator that produces numbers from 1 to 10 one at a time. next() to retrieve each number


def number_generator():
    for i in range(1,11):
        print(i)
        yield
a=number_generator()
for i in range(1,11):
    next(a)
    print("iteration incremented")