class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
      res = set()
      left = set()
      right = collections.Counter(s)

      for i in range(len(s)):
        
        right[s[i]] -= 1
        if right[s[i]] == 0:
            right.pop(s[i])

        for c in range(26):
          char = chr(ord('a') + c)
          if char in left and char in right:
            res.add((s[i], char))
        left.add(s[i])

      return len(res)
# o(nx26) time and o(n) space
# the algorithm creates left and result hashsets...sets to reduce redundancy 
# and a right hashmap because we need the counts of each character 
# we iterate over the string and decrement right at current element by 1 and pop it out if it equals 0
# this means we are processing the current element and also to clean up the right map from useless elements
# we then iterate through the entire alphabet and for every character, if that character is in the left AND right set/map
# we add to res the current character we are iterating through and char in alphabet
# after the entire alphabet is processed we add current element to left and finish iterating through the rest of the string


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
      count = 0
      chars = set(s)
      for c in chars:
        first, last = s.find(c), s.rfind(c)
        count += len(set(s[first+1:last]))
      return count
    
# o(n) time and space
# we keep a count and put s into a hashset
# we iterate over the hashset elements and set find() anf rfind() on the character
# the purpose of this is we use each character as an outer shell and search for suitable mid characters
# since our palindrome can only be length of 3
# once we find the start and end indexes, we add to count the length of the string from first index +1 to last
# the plus 1 is for index purposes...we also add it as a set to eliminate duplicates
# this will return to us the valid palindromes using the current character as the outer shell


# 1930. Unique Length-3 Palindromic Subsequences
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:

# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
# Example 2:

# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
# Example 3:

# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")
 

# Constraints:

# 3 <= s.length <= 105
# s consists of only lowercase English letters.