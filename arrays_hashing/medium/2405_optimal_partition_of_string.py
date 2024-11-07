class Solution:
    def partitionString(self, s: str) -> int:
        l, r = 0, 1
        res = []
        dupes  = {}
        
        while r < len(s):
                if l == r:
                    r += 1

                dupes[s[l]] = 1 + dupes.get(s[l], 0)

                if s[r] not in dupes:
                    dupes[s[r]] = 1 + dupes.get(s[r], 0)
                    r += 1
                else:
                    res.append(s[l:r])
                    l = r
                    r += 1
                    dupes = {}
        return len(res) + 1
    
# my algo...one pass and o(n) space
# my thinking is a sliding window where i add current elements to a hashmap
# if i find something that is already in the hashmap then i will append the correct substring and update pointers while
# also resetting the hashmap to clear it out
# i add one at the end of the return because if the last letter will be its own subarray if it is a duplicate in the subarray before it
# or the last subarray didnt finish with finding a duplicate and wont be added to res
# i couldnt figure out how to start from the first element and edge case of the last element 

# 2405. Optimal Partition of String
# Medium
# Topics
# Companies
# Hint
# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

# Return the minimum number of substrings in such a partition.

# Note that each character should belong to exactly one substring in a partition.

 

# Example 1:

# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.
# Example 2:

# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only English lowercase letters.