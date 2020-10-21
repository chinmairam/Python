"""
You are given a string S with length N.
Determine if it is possible to find two non-empty strings A and B which satisfy the following conditions:

1.A+B=S, where + denotes string concatenation
2.B is a substring of A
"""

t = int(input("Enter no.of testcases:"))
for i in range(t):
    n = int(input("Enter length of string:"))
    s = input("Enter the string:")
    last = s[n-1]
    found = 0
    for j in range(0, n-1):
        if(s[j] == last):
            found = 1
            break
    if(found == 1):
        print("YES")
    else:
        print("NO")
