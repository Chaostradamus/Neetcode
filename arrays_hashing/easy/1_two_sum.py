class Solution(object):
    def twoSum(self, nums, target):
        ans = {}
        for i in range(len(nums)):
          diff = target - nums[i]
          if diff in ans:
            return [ans[diff], i]
          ans[nums[i]] = i


# we will use a hashmap to keep a history of the difference we found
# iterate through nums and calculate the diff as diff = target - current number
# we then check if that diff is in the hashmap because we are guaranteed an answer...so if we find it in the hashmap we have found both answers
# if we cant find it then we insert the number and index as a pair accordingly
# o(n) runtime and space because we create the hashmap and at most have to run through nums once


# example
# first run through we have target(9) minus num(2) = diff(7)
# we chec for 7 in the hashmap thats empty. its not there so we insert 2, 0 into the hashmap
# that means if we eventually find a difference of 2, that means we found the 2's pair that equals the target
# next we have 9 - 7 = 2 for the difference. we check if 2 is in the hashmap...it is so we have a pair of numbers that equals the target
# we return both indexes 
# this works because we are gauranteed to find one pair of answers


# Code
# Testcase
# Testcase
# Test Result
# 1. Two Sum
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
