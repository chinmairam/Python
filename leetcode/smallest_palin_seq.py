"""
a single character is also a palindrome.
So, we just need to print the lexicographically smallest character present in the string.
"""
def short_pal(n, s):
#    return min(s)
    res = s[0]
    for i in range(1,n):
        res = min(res, s[i])
    return res
    

for i in range(int(input())):
    n = int(input())
    str = input()
    ans = short_pal(n, str)
    print(ans)

#Output:
#2
#2
#zy
#y
#1
#cd
#c
