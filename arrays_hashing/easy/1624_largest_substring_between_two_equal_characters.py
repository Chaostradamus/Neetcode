class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
      res = -1

      for i in range(len(s)):
        for j in range(i+1, len(s)):
          if s[i] == s[j]:
            length = (j-i) - 1
            res = max(length, res)
      return res
    
# o(n^2)
# my solutio is double for loops sliding a window from each i to end of string until we find a match and recording the len
# return -1 if not found or max of res and whatever is found


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
      res = -1
      char_index = {}

      for i , c in enumerate(s):
        if c in char_index:
          res = max(res, (i - char_index[c]) - 1)
        else:
          char_index[c] = i
      return res


# optimal solution that is o(n) and constant time space because 26 letter alphabet max
# hold a char_index hashmap that maps each character to it's index as the key value pair
# ie b (element) : 6 (index)
# enumerate through s and if letter is in hashmap then we already found one and dont need to add it
# because we want the first occurence of the letter and everything inbetween even if we find another occurence doesnt matter
# ie baaaBaaab we will only count hte first b not the middle b, but at the middle b and end b, we will record lengths to see which one is longer
# if letter is already in hashmap we record the res as the max of res
# or current index minus the char_index of first occurence(which it will record and map first) -1 (for indexing purposes)
# else we found the letter for the first time so we record in hashmap at that character the index 
# ie char_index[character]: index
# return res



# 1624. Largest Substring Between Two Equal Characters
# Easy
# Topics
# Companies
# Hint
# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
 

# Constraints:

# 1 <= s.length <= 300
# s contains only lowercase English letters.