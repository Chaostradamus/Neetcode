class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        
        for n in nums:
          if n in hashset:
            return True
          hashset.add(n)
        return False

# explanation

# loop through the array
# if element we are at is in hashset then there is a duplicate so we return True
# else its not in the hashset so we add it to hashset
# if looping through nums array finishes that means we didnt find a duplicate so we return False outside of the loop
# linear time and spear because it will create a hashset and will also loop through entire array N times


# Code
# Testcase
# Test Result
# Test Result
# 217. Contains Duplicate
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true