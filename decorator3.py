def cube(func):
    def wrapper(arg):
        return func(arg)**3
    return wrapper

@cube
def num(x):
    return x

print(num(3))
