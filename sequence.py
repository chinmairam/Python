def sequence(n):
   while n != 1:
    print(n)
    if n%2 == 0:
      n = n/2
    else:
     n = n*3+1
print("Enter value of n")
n = int(input())
s = sequence(n)
print("Sequence is ",s)
