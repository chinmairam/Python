A = []
for i in range(int(input())):
    k = int(input())
    A.append(k)
    sum1 = []
for x in A:
    p = list(filter(lambda y: y != x, A))
    sum1.append(sum(p))
print(min(sum1))
