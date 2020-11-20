"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
"""

class Solution:
    def helper(self, top, bottom, match):
        count = 0
        for i in range(len(top)):
            if top[i] != match:
                if bottom[i] == match:
                    count += 1
                else:
                    return 30000
        return count

    def minDominoRotations(self, A, B):
        top_a = self.helper(A, B, A[0])
        bot_a = self.helper(B, A, A[0])
        top_b = self.helper(A, B, B[0])
        bot_b = self.helper(A, B, B[0])
        m = min(top_a, bot_a, top_b, bot_b)
        return -1 if m == 30000 else m

s = Solution()
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
x = s.minDominoRotations(A, B)
print(x)
