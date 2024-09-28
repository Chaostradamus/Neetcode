class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      res = [1] * len(nums)
      for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]
      postfix = 1
      for i in range(len(nums) -1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
      return res
    

# this idea is a two pass from left to right then right to left of the nums array
# the first pass stores the current element's products to the left...we will also store this in a new res array to return as the answer
# on the way back from right to left we have to store a variable we will call postfix
# this variable will hold everything to the right of the current element
# we will initialize it as 1 to start because the last element will just remain the same so we will just multiply by 1
# we will take the currently last element in res array and multiply it by the post fix
# we then set postfix of 1 equal to postfix times the nums array at the same iteration
# this will keep track of every product to the right of current element
# 
# as we iterate backwards we will keep multiplying res at current index to postfix 
# and then setting postfix to postfix time current identitcal index of nums array
# the idea is traverse left to right storing current elements left side products to the left...then on the way back from
# right to left we keep a variable to track current elements right side products
# we multiply them and set it as new res at ith index and then update postfix variable to postfix times nums of ith
# to accurately track the right side of next current element


# 238. Product of Array Except Self
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.