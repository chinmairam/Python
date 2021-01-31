def round(n):
    a = (n//10)*10
    b = a + 10
    return b if n-a>b-n else a

t = int(input())
for _ in range(t):
    n  = int(input())
    print(round(n))
        
