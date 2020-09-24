# Generator Expressions
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) +1 ):
        if x % i == 0:
            return False
    return True

million_squares = (x*x for x in range(1,1000001))
print(million_squares)
print(list(million_squares)[-10:])
print(list(million_squares))
# Sum of first 10 million squares
print(sum(x*x for x in range(1,10000001)))
print(sum(x for x in range(1001) if is_prime(x)))
