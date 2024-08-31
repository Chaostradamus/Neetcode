class Solution:
    def makeEqual(self, words: List[str]) -> bool:
      char_count = defaultdict(int)

      for w in words:
        for c in w:
          char_count[c] += 1

      for c in char_count:
        if char_count[c] % len(words):
          return False
      return True
    
# o(n) runtime cause one pass through and constant time space because it tops out at 26 letters in the alphabet as a possibility
# the key is that we can redistribute all characters as we please, we do not need each word to be the same characters in their current orders
# if it were then it would be majorly complex for a leetcode easy
# knowing this, we can just take count of every characters in all words in a hashmap
# we will have each element's total count
# we then divide each character count by the number of words, if no remainder then each word can get an equal amount of that character
# if there are remainders then we cannot distribute evenly thus we return false
# code is to create a default dict set with an int so if we run into first occurence or no occurence of character it will set to 0
# we populate the hashmap word by word character in word by character
# we then check for every count % NUMBER OF WORDS to see if we can evenly distribute
# we do not do by length of elements in hashmap because this will falsely return wrong answer
# return true if we find no remainders % len(words)

# scenario where dividing by len of hashmap vs words comes into play below

# Let's look at a different scenario where your original logic might return the wrong result:

# Example: words = ["aaa", "bbb", "ccc", "abc"]
# Total Character Counts:
# a: 4 times
# b: 4 times
# c: 4 times
# Here, the char_count dictionary would be:

# python
# Copy code
# {'a': 4, 'b': 4, 'c': 4}
# Original Code Logic:
# Your original code checks if the count of each character is divisible by the number of distinct characters (len(char_count)), which is 3:

# python
# Copy code
# if char_count[c] % len(char_count) != 0:
#     return False
# For a, 4 % 3 = 1 (remainder 1), so the condition fails, and the code would correctly return False here.
# For b, 4 % 3 = 1 (remainder 1), so the condition fails again.
# For c, 4 % 3 = 1 (remainder 1), so the condition fails again.
# However, this is not an example of incorrect behavior; it's still correctly returning False.

# Scenario Where the Logic Could Fail:
# Let's consider a slight modification:

# Example: words = ["aaab", "bbbc", "ccca", "abc"]
# Total Character Counts:
# a: 4 times
# b: 5 times
# c: 5 times
# The char_count dictionary would now be:

# python
# Copy code
# {'a': 4, 'b': 5, 'c': 5}
# Applying Your Original Logic:
# Your original code checks if the count of each character is divisible by the number of distinct characters (len(char_count)), which is still 3:

# For a, 4 % 3 = 1 (remainder 1), so the condition fails, and the code would correctly return False.
# For b, 5 % 3 = 2 (remainder 2), so the condition fails again.
# For c, 5 % 3 = 2 (remainder 2), so the condition fails again.
# But here's the twist:

# If the Number of Words Was Different:
# If we had more words, say, words = ["aaab", "bbbc", "ccca", "abcd", "abcd"]:

# Total Character Counts:
# a: 5 times
# b: 6 times
# c: 6 times
# d: 2 times
# If we incorrectly divide by the number of unique characters instead of the number of words (which would be 5 here), the code might incorrectly return True when it should not, because the checks might accidentally align, especially if the characters' counts somehow seem to distribute "evenly" by the wrong divisor.

# Conclusion:
# While in many cases your code might return the correct result (False), the fundamental issue is that it uses an incorrect divisor (len(char_count) instead of len(words)). This could lead to incorrect results in cases where the number of unique characters doesn't align with the intended distribution across words. It’s important to use the correct divisor to ensure accuracy in all cases.

# how to not use built in library for defaultdict
# char_count = {}

# # Sample string for counting characters
# words = ["example", "words", "here"]

# # Iterate over each word and character
# for word in words:
#     for char in word:
#         # Increment the character count, using .get() to handle missing keys
#         char_count[char] = char_count.get(char, 0) + 1

# print(char_count)

# 1897. Redistribute Characters to Make All Strings Equal
# Easy
# Topics
# Companies
# Hint
# You are given an array of strings words (0-indexed).

# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

# Return true if you can make every string in words equal using any number of operations, and false otherwise.

 

# Example 1:

# Input: words = ["abc","aabc","bc"]
# Output: true
# Explanation: Move the first 'a' in words[1] to the front of words[2],
# to make words[1] = "abc" and words[2] = "abc".
# All the strings are now equal to "abc", so return true.
# Example 2:

# Input: words = ["ab","a"]
# Output: false
# Explanation: It is impossible to make all the strings equal using the operation.
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.