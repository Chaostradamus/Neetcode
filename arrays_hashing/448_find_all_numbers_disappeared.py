class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
          i = abs(n) -1
          nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
          if n > 0:
            res.append(i +1)
        return res
    

# o(n) runtime and constant time space except for the res array which leetcode doesnt count
# we iterate through nums first and we make it negative
# this signifies that the number exists and marked through the INDEX of nums
# then we go through newly fixed nums array and if at that index the nunebr is positive, we know thorugh the INDEX that the number is missing so we append the i +1 to result

# 448. Find All Numbers Disappeared in an Array
# Easy
# Topics
# Companies
# Hint
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 