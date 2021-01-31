from functools import reduce
N = int(input())
A = list(map(int, input().split()))[:N]
m = int(input())
B = [[0 for j in range(2)] for i in range(m)]
for i in range(m):
    for j in range(2):
        k = int(input())
        B[i][j] = k

count = [0]*len(B)
X = []
for p,l in B:
    X = A[p:l+1]
    res = reduce(lambda x, y: x & y, X)
    #res = [X[i]%X[j] for i in range(len(X)) for j in range(len(X))]
    print(res)
    if res<=0:
        for i in range(len(X)):
            X[i] += 1
            res = res&X[i]
            if res>0:
                count[X[i]] += 1
                break
    else:
        continue
print(count)
