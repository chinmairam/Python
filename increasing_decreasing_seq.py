"""You are given a sequence of n integers a1,a2,---,an.
You have to construct two sequence of integers b and c with length n that satisfy:
  1. for every i (1<= i <= n): bi+ci=ai
  2. b is non-decreasing which means that for every 1< i <= n,bi>=bi-1 must hold
  3. c is non-increasing,ehich means that for very 1<= i <=n, ci<=ci-1 must hold
You have to maximize max(bi,ci)
In othr words,you have to minimize the maximum number in sequences
b and c.
"""
# Increase is handled by b (b is ascending)
  # If b[0] = num
  # Maximum in b is sum of all increases (last element in b) (num + sum of all increases)
# Decrease is handled by c (c is descending)
  # Maximum in c is the first number in c(a[0]-num)

# sum of all increases = diff
# ans = max(num+diff,a[0]-num)
# num+diff = a[0]-num (Go until max(b) = max(c))
# num = a[0]-diff/2
# final answer will be a[0]+diff/2

T = int(input("Enter no.of testcases:"))

for case in range(T):
    n = int(input("Enter size of array:"))
    arr = list(map(int, input().split()))

    diff = 0
    for i in range(1 ,len(arr)):
        if arr[i] > arr[i-1]:
            diff += (arr[i] - arr[i-1])
    ans = (diff + arr[0])//2 # Divide an odd number into two.
    ans  = max(ans, diff+arr[0] - ans)

    print(ans)
    
#Enter no.of testcases:2
#Enter size of array:4
#2 -1 7 3
#5
#Enter size of array:6
#-9 -10 -9 -6 -5 4
#3

