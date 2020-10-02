from random import seed
from random import random
seed(1)
def randomList(n):
 s = [0] * n
 for i in range(n):
   s[i] = random()
 return s
n = int(input("Enter a number"))
print(randomList(n))
