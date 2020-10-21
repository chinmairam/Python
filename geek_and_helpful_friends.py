"""
Geek has N friends who are willing to help him make the final problem for Codejuring Contest.
Each of his ith friend has arr[i] probability of coming up with a good problem. 
Geek will be upset if no one is able to come up with a problem or if he ends up with more than 1 problem.
Can you help Geek decide which set of people he should ask for help so that the chances of him getting upset are minimum ? 
Find the optimal probabilty of him getting exactly one problem.
"""

import math

class Solution:
	def solve(self, arr, n):
		arr.sort()

		i = 0
		while i < (n//2):
			tmp = arr[i]
			arr[i] = arr[n-i-1]
			arr[n-i-1] = tmp
			i+=1

		if arr[0] == 1.00000000000000000:
			return 1.000000000000000

		dp = [0.000000000 for _ in range(n)]
		on = 1.000000000
		dp[0] = arr[0]
		fans = dp[0]
		prod = on - arr[0]

		for i in range(1,n):
			dp[i] = (on - arr[i]) * dp[i-1] + prod * arr[i]
			if dp[i] > fans:
				fans = dp[i]
			prod *= (on - arr[i])

		return fans

def main():

    T = int(input("Enter no.of inputs:"))

    while(T > 0):
        N = int(input("Enter no.of friends:"))
        arr = [float(x) for x in input("Enter array elements:").strip().split(" ")]
        ob = Solution()
        print('%.9f'%ob.solve(arr, N))

        T -= 1

if __name__ == "__main__":
    main()

"""
Input:
N = 4
arr[] = {0.1, 0.2, 0.3, 0.8}

Output:
0.800000000000

Explanation: The best strategy for Geek 
is to ask only one of his friends, the 
most reliable one.
"""
