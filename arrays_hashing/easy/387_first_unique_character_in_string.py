class Solution:
    def firstUniqChar(self, s: str) -> int:
      count = Counter(s)
      
      for i in range(len(s)):
        if count[s[i]] == 1:
          return i
      return -1

# create a default dictionary and declare it with an int to prevent key error 
# this prevents finding a count of 0 and returning an error although we can just use the .get()
# populate the count hashmap
# iterate through s and return index of element if in the hashmap current element value is 1


    #   class Solution:
    # def firstUniqChar(self, s: str) -> int:
    #   count = defaultdict(int)

    #   for c in s:
    #     count[c] +=1 
    #   for i, c in enumerate(s):
    #     if count[c] == 1:
    #       return i
    #   return -1


      # count = Counter(s)
      
      # for i in range(len(s)):
      #   if count[s[i]] == 1:
      #     return i
      # return -1

# o(n) runtime and space
# get a count of letters in s
# iterate through s while comparing current element to count at the character
# if it equals 1 then we found an occurence of a single character in string
# return index as soon as we find a match
# my algo beats neetcode by about 10%



# 387. First Unique Character in a String
# Easy
# Topics
# Companies
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.