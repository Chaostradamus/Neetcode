class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      i, j = 0, 0
      while i < len(s) and j < len(t):
        if s[i] == t[j]:
          i += 1
        j += 1
      return i == len(s)
    
# i tried looping through both with nested loops again wheni just needed one pass
# i tried traverse s and nesting a traversal of T inside it...if a character matched then match variable +=1 
# we check if match = length of S signaling it is a subsequence and return true
# false if not

# opmtimal solution would be to have pointers..2...one on each string
# while both in bounds , we compare the paired elements in both strings...if they are equal we increase s's pointer
# we increase t's pointer in every case
# we return true if i is the same value as the length of S
# the pointers act as a counter as well as a pointer

# 392. Is Subsequence
# Easy
# Topics
# Companies
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 