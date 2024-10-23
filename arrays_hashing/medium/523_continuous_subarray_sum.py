class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
      total = 0
      remainder = {0: -1}

      for i , n in enumerate(nums):
        total += n
        r = total % k
        if r not in remainder:
          remainder[r] = i
        elif i - remainder[r] > 1:
          return True
      return False


# o(n) time and space because one pass and hashmap space
# kind of like twosum where we put the difference as key and index as value
# we calculate each continous subarrays remainder
# if at some point the current subarrays remainder is the same as an previous, then we know we found a viable subarray
# for example for k = 6 and nums 23, 2, 4, 6, 7
# 25 % 6 = 5
# when we reach 23, 2, and 4 the total will be 29 and the remainder will again be 5
# this means we found a viable subarray because if we found another subarray with remainder of 5
# we added a subarray that equals 0 to the first subarray that had a remainder of 5 which means its a multiple of 6
# we subtract current index by the first subarray with the same remainder and chec if the length is greater than 1
# inthat case we return true else after the loop runs we return false

# we set total to 0 and create a hashmap with 0: mapped to -1 to start
# we enumerate through nums and add current element to total and divide it by k to find remainder
# we check if that remainder is in hashmap yet, if not we add it using remainder as key and index as value
# if remainder is in hashmap already we will check if current index minus remainder's index > 1 and return true
# if we dont find a viable array we will return False


# Case 1: Valid subarray from the start
# Consider the array nums = [5, 5] and k = 5.

# The algorithm initializes total = 0 and remainder = {0: -1}.
# When it starts iterating:
# At i = 0:
# total = 5
# r = total % k = 5 % 5 = 0
# Since r = 0 is already in the hashmap (from {0: -1}), we check the index difference: i - remainder[r] = 0 - (-1) = 1, which is not greater than 1, so we continue.
# At i = 1:
# total = 10
# r = total % k = 10 % 5 = 0
# Now the index difference is i - remainder[r] = 1 - (-1) = 2, which is greater than 1, so we return True because the subarray [5, 5] is valid and its sum is divisible by k.
# If we hadn’t initialized remainder with {0: -1}, the algorithm wouldn't detect that the sum of the first two elements ([5, 5]) is divisible by k.

# Case 2: Why {0: -1} is needed
# The -1 index allows us to handle subarrays that start right at the beginning of the array. Without this initialization, when r = 0 is encountered for the first time (after adding the first element), there would be no earlier index to compare with, and the algorithm wouldn’t recognize that the sum up to that point is divisible by k.

# In short, initializing with {0: -1} ensures that the algorithm can detect valid subarrays starting from the beginning of the array. It provides a "virtual starting point" before the actual array begins.



# 523. Continuous Subarray Sum
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1