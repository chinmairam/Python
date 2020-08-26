# The "timeit" module lets you measure the execution
# time of small bits of Python code

import timeit

x = timeit.timeit('"-".join(str(n) for n in range(100))',
                       number=10000)

y = timeit.timeit('"-".join([str(n) for n in range(100)])',
                       number=10000)

z = timeit.timeit('"-".join(map(str, range(100)))',
                       number=10000)

print(x)
print(y)
print(z)
