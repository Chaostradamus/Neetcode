class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      count = 0
      total = 0
      dic = {0:1}
      


      
      for i in range(len(nums)):
        total += nums[i]
        if total - k in dic:
          count += dic[total-k]
        dic[total] = 1 + dic.get(total, 0)
      return count


# one pass and one data structure to hold counts so o(n) time and space
# the thought process is the similar to 2 sum
# whereas in two sum we iterate through each element and subtract it from target..if the answer is in hashmap
# then we found its complementing pair

# in this question we will instead of 1 off equations, we will keep a running count and subtract k from it
# if the complement is found in hashmap then we add that differences count to our count of contiguous subarrays
# this shows that with current elements, we found a way to reach the target number
# no matter what we will increase the current running totals count by 1 
# and return count

# first we create a count and total variable where count is number of subarrays hit target
          




# 560. Subarray Sum Equals K
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107