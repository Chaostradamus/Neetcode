class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j 
            
        return res

# to encode
# create new res string
# iterate through every word in strings and concatenate the length of the word + "#" + string

# to decode
# create a new res string
# set j variable to i to reset j to i every time we find a word and append to res
# iterate through each character with 2 pointers
# one pointer will iterate through each character until a # delimiter is found
# we will take previous character before the # as a int which will tell us the length of the word
# we will append to res the position of j +1 to the length +1
# j+1 gets us to first character of the word and off the #
# length + 1 gets us to the end of the word ...the +1 is not inclusive so we need ti index it out 1 more space
# we update i to j + length + 1 to get to the end of that word



# Problem Description
# Encode and Decode Strings

# Encoding:

# You need to convert a list of strings into a single string.
# Each string in the list should be prefixed with its length and a delimiter (like #).
# For example, the list ["hello", "world"] would be encoded as "5#hello5#world".
# Decoding:

# Given the encoded string, you should be able to convert it back into the original list of strings.
# You need to read the length of each string from the encoded string and extract the corresponding string using that length.
# Implementation Steps
# Encoding
# For each string in the list:
# Get the length of the string.
# Concatenate the length, a delimiter (e.g., #), and the string itself.
# Decoding
# Read the encoded string.
# Use the delimiter to find the length of each string.
# Extract the string based on the previously read length.
# Example
# Input: ["hello", "world"]
# Encoded: "5#hello5#world"
# Decoded: ["hello", "world"]

# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.