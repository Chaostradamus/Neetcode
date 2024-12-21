class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        substring = set()
        res = set()
        i = 0
        while i < len(s) - 9:
            sub = s[i:i+10]
            if sub in substring:
                res.add(sub)
            else:
                substring.add(sub)
            i +=1
        return list(res)
    

# o(N) time and space
# had toe exact same answer as neetcode but forgot to increment i........... rookie mistake
# we are adding every substring of 10 length to a hashset to take out dupes and to check if there are dupes in S
# create two sets or arrays or whatever data structure to hold the res and substrings
# we check every length of 10 substring till the end. -9 for indexing because it starts at 0
# if that current substring isnt in substring set then add to result set...if its in res set then it wont be added
# else its not in substring set yet and will be added
# return result as a list

        


# 187. Repeated DNA Sequences
# Medium
# Topics
# Companies
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either 'A', 'C', 'G', or 'T'.