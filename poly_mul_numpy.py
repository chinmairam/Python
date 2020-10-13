import numpy as np
p1 = np.poly1d([1,2])
p2 = np.poly1d([4,9,5,4])

print("p1 : ", p1)
print("\n p2 : \n", p2)

mul = np.polymul(p2, p1)
print("\n\npoly1D object : ")
print("Multiplication Result : \n", mul)
