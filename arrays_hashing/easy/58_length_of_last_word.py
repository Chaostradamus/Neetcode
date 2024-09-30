class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        for i in range(len(s) -1, -1, -1):
            if s[i] == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c
    
# i tried keeping a count variable and then starting from the back of the string
# increasing the count   then checking if it was a blank character..if so exit and return
# this doesnt take into account if the string starts with white spaces from the back
# the correct logic is to traverse the string from the back...checking if its a blank space..
# we then check if count is greater than or equal to 1...we return the count...if count >= 1 that means we started a word count and encountered a blank
# thus finding the length of the last word...the else statement for the OUTER if statement increases count..signifying finding a character

# this way helps us check for starting blank spaces by only incrementing if we find a non black space...and if we find a multiple blanks..
# count will tell us whether we started counting for a word or not

# Code
# Testcase
# Test Result
# Test Result
# 58. Length of Last Word
# Solved
# Easy
# Topics
# Companies
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.