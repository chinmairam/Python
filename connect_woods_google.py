"""There are n pieces of wood A, m pieces of wood B.
1st piece of wood A has two parameters Li,ri which indicates that it can combine
with any piece of wood B that has length betwen Li and ri(both inclusive).
Also for each piece of wood B we are given its length.
The aim is to associate each piece of wood A,with some piece of wood B following the
above condition.Each piece of wood B can be used atmost once.
Find if this is possible or not."""

# Wood A length ranges:(3,7),(1,3),(2,5)
# Wood B lengths:4,8,5,3
# Possible allotments:
#   (3,7) -> 4,5,3
#   (1,3) -> 3
#   (2,5) -> 4,5,3
# 1st possibility:
#   (3,7) -> 4
#   (1,3) -> 3
#   (2,5) -> 5
# 2nd possibility:
#   (3,7) -> 5
#   (1,3) -> 3
#   (2,5) -> 4

# Observation:
# 1.Not all type_B needs to be alloted
# 2.All type_A must be alloted

from bisect import bisect_right

n,m = list(map(int, input().split()))
type_A = []

for i in range(n):
    span = list(map(int,input().split()))
    type_A.append(span)

type_B = list(map(int, input().split()))

type_A.sort(key = lambda x: (x[0],x[1]))
type_B.sort()

found = True

for i in range(len(type_A)-1, -1, -1):
    current_left = type_A[i][0]
    current_right = type_A[i][1]

    pos = bisect_right(type_B, current_right, 0, len(type_B))
    # bisect_right(name of list, key searching for, from , to)
    current_piece = type_B[pos-1]

    if current_left <= current_piece:
        del type_B[pos-1]
    else:
        found = False
        break

if not found:
    print("NO")
else:
    print("YES")
    
#3 4
#3 7
#1 3
#2 5
#4 8 5 3 
#YES
