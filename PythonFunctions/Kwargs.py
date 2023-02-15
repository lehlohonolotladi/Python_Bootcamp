def my_func(*args):
    return sum(args), max(args)


print(my_func(1, 2, 3, 4))


# This one again
def my_func(a, b=2):
    a += b
    print(f'a is {a} and b is {b}')


my_func(b=3, a=2)


# Another one from the Queries
def add(a, b=1, c=2):
    return a + b + c

print(add(10, 20))

#From the quiz
def f1(a=0, b=1, c=2):
    return a + b + c, a - b - c, a * b * c


print(f1(3, 4))