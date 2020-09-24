import datetime

def timer(func):
    def wrapper():
        start = datetime.datetime.now()
        func()
        runtime = datetime.datetime.now() - start
        print(runtime)
    return wrapper

@timer
def pointless():
    for i in range(20000000):
        x = i*2
    print(x)
pointless()

def repeat(func):
    def wrapper():
        for i in range(2):
            func()
            print(i)
    return wrapper

@timer
@repeat
def pointless():
    for i in range(20000000):
        x = i*2
    print(x)
pointless()