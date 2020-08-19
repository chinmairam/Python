from math import factorial

f = [len(str(factorial(x))) for x in range(20)]
print("List Comprehension: ")
print(f)

s = {len(str(factorial(x))) for x in range(20)}
print("Set Comprehension: ")
print(s)
