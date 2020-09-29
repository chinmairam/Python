"""Given a string s of length n.Choose any subsequence
of length n-1,which appears first in the dictionary order
among other subsequences of same length"""

# n = 4
# s = abcda
# sequences of length 4:['bcda','acda','abda','abca','abcd']
# After sorting, abca occurs first in dictionary order.

n = int(input("Enter length of string:"))

s = input("Enter the string:")

change = -1

for index in range(len(s)-1):
    if s[index] > s[index+1]:
        change = index   # 'd'> 'a'
        break

answer = ''

if change >= 0:
    answer = s[:change] + s[change+1:]
else:
    answer = s[:-1]

print(answer)
