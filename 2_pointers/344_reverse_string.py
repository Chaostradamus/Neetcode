class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      res = ""

      for i in range(len(strs[0])):
        for s in strs:
          if i >= len(s) or s[i] != strs[0][i]:
            return res
        res += strs[0][i]
      return res

# 344. Reverse String
# Easy
# Topics
# Companies
# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.