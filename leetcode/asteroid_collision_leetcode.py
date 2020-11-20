"""We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.
             The 5 and 10 never collide.

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right.
             Asteroids moving the same direction never meet,
             so no asteroids will meet each other.
"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for new in asteroids:
            # does it collide?
            while ans and new < 0 and ans[-1] > 0: # till ans is not empty
                # there is a possibility collide
                if ans[-1] < -new:
                    ans.pop()
                    continue # negative asteroid not broken here,continue till broken
                elif ans[-1] == -new: # abs[-1] + new = 0
                    ans.pop()
                    break
                else: # res[-1] > -new:
                    break
            else:
                ans.append(new) # if while fails
        return ans

s = Solution()
asteroids = [5, 10, -5]
x = s.asteroidCollision(asteroids)
print(x)

# Using Stack.
