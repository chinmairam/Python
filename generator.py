# Generators

def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
print(g)
for i in range(3):
    print(next(g))

for v in gen123():
    print(v)

h = gen123()
j = gen123()
print(h)
print(j)
# h and j are different objects 
print(h is j)
