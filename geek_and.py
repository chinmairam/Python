"""Geek has devised a special problem to test your skill. 
Given an array of numbers and Q queries such that each query consists of two numbers l and r.
For each query, find the minimum number of increment operations (adding one to a number)
  that need to be performed on the array elements between the indexes l and r such that their bitwise AND is greater than zero.
Note: Follow 0 based indexing."""
class Solution:
	def geekAnd(self, n, a, q, queries):
		a.insert(0,0)
		n = n + 1
		dp = [[0 for j in range(32)] for i in range(n)]
		for i in range(n):
			temp = 0
			for j in range(32):
				if (1<<j) & a[i] != 0:
					temp |= 1<<j
				dp[i][j] = int(max(pow(2,j) - temp,0))

		for j in range(32):
			for i in range(1,n):
				dp[i][j] += dp[i-1][j]

		maxValue = int(pow(10,18))

		ans = [maxValue for i in range(q)]

		for i in range(q):
			left = queries[i][0]
			right = queries[i][1] + 1
			

			for j in range(32):
				ans[i] = min(ans[i], dp[right][j] - dp[left][j])

		return ans

if __name__ == "__main__":

    t = int(int(input("Enter no.of inputs:")))

    for tcs in range(t):
        n = int(input("Enter N value:"))
        a= [int(x) for x in input("Enter array numbers:").strip().split(" ")]
        q = int(input("Enter no.of queries:"))
        queries = []
        for _ in range(q):
            temp = [int(x) for x in input().strip().split(" ")]
            queries.append(temp)
        ob = Solution()
        ans = ob.geekAnd(n, a, q, queries)
        for value in ans:
            print(value, end = ' ')
        print()

# Give input as
#Enter no.of inputs:1
#Enter N value:4
#Enter array numbers:1 2 3 1
#Enter no.of queries:3
#0 1
#1 2
#2 3
