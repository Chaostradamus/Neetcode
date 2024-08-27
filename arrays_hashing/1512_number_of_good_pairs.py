class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
      pairs = 0
      for i in range(len(nums) -1):
        for j in range(i+1, len(nums)):
          if nums[i] == nums[j]:
            pairs += 1
      return pairs
    
    # my solution which is just nested for loops 
    # o(n^2)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
      count = {}
      res = 0
      for n in nums:
        if n in count:
          res += count[n]
          count[n] +=1 
        else:
          count[n] = 1
      return res
    

# o(n) solution:
# use hashmap and res counter to 0
# ierate through nums 
# if we see a number thats already in the hashmap we add that numbers count to res WHICH IS RESET TO 0 SO WE DONT KEEP ADDING PREVIOUS PAIRS
# we add the previous count to 0 before we increase the count of that elements count
# else we set that element in hashmap to 1
# return result after
# this is one pass and more efficient than nested forloops but a little more mathematically involved


# 1512. Number of Good Pairs
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100