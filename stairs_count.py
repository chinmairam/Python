# Python program to count 
# ways to reach nth stair
# The person can climb either 1 stair or 2 stairs at a time.

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Returns no. of ways to  
# reach sth stair 
def countWays(s):
    return fib(s+1)

s = 4
print("Number of ways = ",countWays(s))
