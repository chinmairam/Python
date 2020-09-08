#1
import math as m
def func(*args):
    mean = sum(args)/len(args)
    var = 0
    for i in range(len(args)):
        var += (args[i]-mean)**2
    var = var/len(args)
    return m.sqrt(var)

#2.1
n = int(input("Enter a number"))
d = {}
for j in range(1,n+1):
    if j % 3 == 0:
        d[j] = j**3
print(d)

#2.2
n = int(input("Enter a number"))
z = ((i,i**3) for i in range(1,n+1) if i%3 == 0)
print(dict(z))

#2.3
n = int(input("Enter a number"))
di = {i:i**3 for i in range(1,n+1) if i%3==0}
print(di)

#2.4
def generator(x):
    for i in range(1,x+1):
        if i%3 == 0:
            yield i, i**3
d = {}
x = int(input("Enter a number"))
for x,j in generator(x):
    d[x] = j
print(d)
   



