import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

np_baseball = np.array(baseball)

print(np_baseball)
print(type(np_baseball))


x = [4 , 9 , 6, 3, 1]
print(x[1])
y = np.array(x)
print(y[1])
""" For numpy specifically,
you can also use boolean numpy arrays."""
high = y > 5
print(y[high])
