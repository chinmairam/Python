class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs) #returns f value

@CallCount
def hello(name):
    print('Hello, {}!'.format(name))

#print(hello.__call__)
hello('Fred')
hello('Wilma')
hello('Betty')
hello('Barney')
print(hello.count)

#Python calls an instance's __call__() when it's used as a decorator.
#__call__()'s return value is used as a new function.
 
