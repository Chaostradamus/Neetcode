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

# https://pythontutor.com/render.html#code=from%20typing%20import%20List%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20longestCommonPrefix%28self,%20strs%3A%20List%5Bstr%5D%29%20-%3E%20str%3A%0A%20%20%20%20%20%20res%20%3D%20%22%22%0A%0A%20%20%20%20%20%20for%20i%20in%20range%28len%28strs%5B0%5D%29%29%3A%0A%20%20%20%20%20%20%20%20for%20s%20in%20strs%3A%0A%20%20%20%20%20%20%20%20%20%20if%20i%20%3E%20len%28s%29%20or%20s%5Bi%5D%20!%3D%20strs%5B0%5D%5Bi%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20res%0A%20%20%20%20%20%20%20%20%20%20res%20%2B%3D%20strs%5B0%5D%5Bi%5D%0A%20%20%20%20%20%20return%20res%0A%0A%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.longestCommonPrefix%28%5B%22flower%22,%22flow%22,%22flight%22%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

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