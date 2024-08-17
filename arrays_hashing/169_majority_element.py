class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      count = {}
      res, maxC = 0, 0

      for n in nums:
        count[n] = 1 + count.get(n, 0)
        res = n if count[n] > maxC else res
        maxC = max(count[n], maxC)
      return res


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      res , count = 0, 0

      for n in nums:
        if count == 0:
          res = n
        count += (1 if n == res else -1)
      return res



# 169. Majority Element
# Solved
# Easy
# Topics
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2      

# solution 1
# set a res and max count to keep track of res and current max
# set count hashmap
# iterate through nums and add to count hashmap while comparing if that current element's count is higher than res and then update maxCount
# return res
# this is o(n) because it runs through every element once


# solution #2 is boyer moore algo
# o(1) space because we dont need the hashmap but still o(n) runtime
# we depend on the constraint that there is guaranteed to be one answer
# we iterate through nums and if count is currently 0 then res will = current element
# we add 1 to current count is element matches res else we decrement by 1
# return res after all is done