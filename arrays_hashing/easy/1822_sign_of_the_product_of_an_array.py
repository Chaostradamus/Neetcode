class Solution:
    def arraySign(self, nums: List[int]) -> int:
      res = 1
      for n in nums:
        res *= n
      if res < 0:
        return -1
      elif res == 0:
        return 0
      else:
        return 1
      
# my solutiion runs o(n) time and constant space unless you count the variable
# we iterate and multiply res =1 by each element and return accordingly depending on the sign of the end product

class Solution:
    def arraySign(self, nums: List[int]) -> int:
      neg = 0
      for n in nums:
        if n == 0:
          return 0
        elif n < 0:
          neg += 1
      return -1 if neg % 2 else 1
    
# neetcode answer 
# idea is to only count negative numbers because my solution and any other solution that multiplies the elements
# may overflow with a number that is too large. python prob doesnt have this problem but other languages will
# we iterate and count the number of negatives. if we find a 0 tho we return 0 because the product will be a 0
# if we find a 0 at any point
# at the end we return -1 if neg % 2 else 1
# the above means we will return -1 if neg % 2 returns a 1 which means its odd...if it return sa 0 that means its even
# return -1 if neg %2 returns a truthy falsy based on the answer....anything other than a 0 is a truthy while a 0 is falsy



# 1822. Sign of the Product of an Array
# Easy
# Topics
# Companies
# Hint
# Implement a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product).

 

# Example 1:

# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1
# Example 2:

# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0
# Example 3:

# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
 

# Constraints:

# 1 <= nums.length <= 1000
# -100 <= nums[i] <= 100