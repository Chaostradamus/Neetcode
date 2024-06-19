class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      
      cS, cT = {}, {}

      for i in range(len(s)):
        cS[s[i]] = 1 + cS.get(s[i], 0)
        cT[t[i]] = 1 + cT.get(t[i], 0)
      return  cS == cT

# o(n) runtime and space
# return false is lengths of strings are not equal because they wont match obviously
# populate each hashmap with contents of each string. we use .get on the hashmap because it might be a 0 count and throw an error
# return if both hashmaps are equal which will return true or false depending on the match


# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false