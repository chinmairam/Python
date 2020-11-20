"""
Given an array of integers taht is already sorted in ascending order,
  find two numbers such that they add up to a specific target
The function twoSum should return indices of two numbers such that they add up to the target,
  where index must be less than index.
Note:
   Your returned answers (both index1 and index2 ARE NOT ZERO-based)
   You may assume that each input would have exactly one solution and
     you may not use the same element twice.
"""

class Solution:
    def twoSum(self, nums, target):
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i+1, j+1]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1

s = Solution()
nums = [2,7,11,15]
target = 9
x = s.twoSum(nums, target)
print(x)
