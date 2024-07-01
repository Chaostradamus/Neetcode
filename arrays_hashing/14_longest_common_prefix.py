class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      res = ""

      for i in range(len(strs[0])):
        for s in strs:
          if i >= len(s) or s[i] != strs[0][i]:
            return res
        res += strs[0][i]
      return res
    
# insanely difficult on first couple tries even with code

# set res variable
# for i in range length of the first string
#   could be the range of any of the strings, it doesnt really matter...length check will happen again later
# then for every string in strs array
# we will check if i is >= to the length of current string
#   this is a second boundary check ...we use >= because greater than will have us out of bounds by 2. we could also use ==
# also on that same check we check if the current strings ith letter is the same as the for loop's strings ith letter
# for example
#  flower flow and float...it will check each strings ith letter against flower one by one and add the letter after the entire array is done iterating
# or it will jump out early because we found a different letter or one of the words are shorter than the others
# return res after


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