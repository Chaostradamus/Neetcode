class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      numSet = set(nums)
      longest = 0

      for n in numSet:
        if (n -1) not in numSet:
          length = 1
          while (n+length) in numSet:
            length += 1
          longest = max(longest, length)

      return longest


# o(n) time and space because we go through each element less than n times because of the set and space because
# we need the hashset
# the idea is to put nums into a set to remove duplicates
# create a longest variable for the result
# we will iterate over numSet and not nums because if we iterate over nums then we repeat processes on duplicate elements
# we first check if there is a previous element by checking if n-1 is in the set
# if there isnt then we know this is the start of a sequence and not mid sequence
# if we find a valid starter element we set a length variable to 1
# we will the use a while loop to check if n+ length is in the numSet
# once we break out of it we take the max of length and longest
# return longest


# 128. Longest Consecutive Sequence
# Solved
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109