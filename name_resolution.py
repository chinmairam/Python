g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    inner()

outer()
#outer.inner() #AttributeError
