class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
      # ans = nums + nums
      # return ans
      ans = []

      for i in range(2):
        for n in nums:
          ans.append(n)
      return ans
    
# i just concatted nums + nums and returned
# neetcode way was to go through nums twice and append each element in nums to ans...so we will go through 2 loops of that
# o(2n) runtime and answer where n is number of elements in nums
# if interviewer asks for more than 2 loops we can change range variable to x

# 1929. Concatenation of Array
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:

# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
 