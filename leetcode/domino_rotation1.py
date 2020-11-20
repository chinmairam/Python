"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
"""

class Solution:
    def minDominoRotations(self, A, B):
        a_counts = [0] * 7
        b_counts = [0] * 7

        same = 0

        for i in range(len(A)):
            a_counts[A[i]] += 1
            b_counts[B[i]] += 1
            print("A=",a_counts)
            print("B=",b_counts)
            if A[i] == B[i]:
                same += 1
        print(same) # same in A and B
        for i in range(1, 7):
            if a_counts[i] + b_counts[i] - same == len(A):
                return len(A) - max(a_counts[i], b_counts[i])
            
        return -1
        

s = Solution()
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
x = s.minDominoRotations(A, B)
print("Min.rotations are:",x)
