#enclosing enclosed(nonlocal)
def exp(n):
    #n = 1
    def num(x):
        #nonlocal n
        return x**n
    return num

square = exp(2)
print(square)
print(square(2))
cube = exp(3)
print(cube(3))
