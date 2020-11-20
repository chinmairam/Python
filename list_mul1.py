##n = int(input())
##for i in range(n):
##    N = input()
##    for i in range(int(N)):
##        arr = input().split()[:int(N)]
##        product = 1
##        for num in arr:
##            product *= int(num)
##        print(product)
##

for x in range(int(input())):
    _ = input()
    mul = 1
    for y in input().split():
        mul *= int(y)
    print(mul)
