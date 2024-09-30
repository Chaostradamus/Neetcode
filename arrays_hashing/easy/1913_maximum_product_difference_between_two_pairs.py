class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
      nums.sort()
      largest = nums[len(nums)-1] * nums[len(nums)-2]
      smallest = nums[0] * nums[1]
      return largest - smallest

# logN solution where we sort and then take the first 2 as min and last 2 as max and do the math part

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
      m1, m2 = 0, 0
      sm1, sm2 = float("inf"), float("inf")

      for n in nums:
        if n > m2:
          if n > m1:
            m1 , m2 = n, m1
          else:
            m2 = n
        if n < sm1:
          if n < sm2:
            sm1, sm2 =sm2, n 
          else:
            sm1 = n

      return (m1*m2) - (sm1 *sm2)
    
# oN solution that basically is one pass with 4 variables held to check at each and variable manipulation
# for max size
# if element is larger than second largest and then first largest , we shift largest to new element and old largest to 2nd largest
# else that mean its bigger than the 2nd but not 1st so only the 2nd largest will change to new element
# for the smallest we do it in reverse kind of
# we check if element is smaller than the bigger of the smalls first then the smallest
# if it is smaller than both then the smallest is not new element and the 2nd smallest is now the smallest before
# else we found that it is smaller than the 2nd smallest but not the smallest so we only have to change
# the second smallest to the new element and smallest remains unchanged



# 1913. Maximum Product Difference Between Two Pairs
# Solved
# Easy
# Topics
# Companies
# Hint
# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

# Return the maximum such product difference.

 

# Example 1:

# Input: nums = [5,6,2,7,4]
# Output: 34
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.
# Example 2:

# Input: nums = [4,2,5,9,7,4,8]
# Output: 64
# Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
# The product difference is (9 * 8) - (2 * 4) = 64.
 

# Constraints:

# 4 <= nums.length <= 104
# 1 <= nums[i] <= 104