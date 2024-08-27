class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
      plus = True
      minus = True

      for i in range(len(nums)-1):
        if not (nums[i] >= nums[i+1]):
          plus = False
        if not (nums[i] <= nums[i+1]):
          minus = False
      return plus or minus
    


# o(n) runtime and constant time space
# create two booolean flag variables set to increasing or decreasing montonic and both as True initially
# iterate through nums
# we will have 2 checks...if its increasing or decreasing...if its not either set the flags to false
# if at anytime its notincreasing or decreasing it will be flagged false...we can optimize this by having the loop end if both are false
# otherwise it will run through the entire array even after we've found that theyre both false


# 896. Monotonic Array
# Easy
# Topics
# Companies
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

# Example 1:

# Input: nums = [1,2,2,3]
# Output: true
# Example 2:

# Input: nums = [6,5,4,4]
# Output: true
# Example 3:

# Input: nums = [1,3,2]
# Output: false