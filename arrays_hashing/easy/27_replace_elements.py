class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      
      n = len(nums) 
      i = 0

      while i < n:
        if nums[i] == val:
          nums[i], nums[n-1] = nums[n-1], nums[i]
          n -= 1
        else:
          i += 1
      return i
    
# i tried multiple ways of swapping including using a temp variable but you can swap in place in python
# i tried iterating from the back and front
# correct and optimal way is to use two pointers, one from the start and one from the back
# then while i hasnt passed n yet...check if nums[i] == val..if so then we swap them and move n
# else we increment i
# basically if we find something to replace, we swap it and move the back pointer up...else we move the front pointer



# 14. Longest Common Prefix
# Easy
# Topics
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.