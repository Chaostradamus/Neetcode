class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
      words = s.split(" ")
      if len(pattern) != len(words):
        return False
      
      c2w = {}
      w2c = {}

      for c, w in zip(pattern, words):
        if c in c2w and c2w[c] != w:
          return False
        if w in w2c and w2c[w] != c:
          return False
        
        c2w[c] = w
        w2c[w] = c
      return True

# o(N+M) because we go through both lists once
# we split the string by the spaces into a new array of words
# we check if the patterns length and words array length are the same
# we zip through pattern and words
  # zip goes through both iterables at the same time
  # if check for the character in pattern
  # if it exists in the hashmap and its NOT to that word return false
  # if check if that word is in the hashmap and mapped to the correct character else return false
  # we do both ways because initially A can mape to cat then B can map to cat...so when we check the word to character we find that cat is already
  # mapped to A so we can return false

    


# 290. Word Pattern
# Solved
# Easy
# Topics
# Companies
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false