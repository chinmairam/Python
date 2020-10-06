def hello():
    "Print a well-known message."
    print('Hello, world!')

print(hello.__name__)
print(hello.__doc__)
print(help(hello))

def noop(f):
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello():
    "Print a well-known message."
    print('hello world!')

print(help(hello))
print(hello.__name__)
print(hello.__doc__)
