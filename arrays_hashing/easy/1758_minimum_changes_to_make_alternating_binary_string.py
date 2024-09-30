class Solution:
    def minOperations(self, s: str) -> int:
        count1, count2 = 0, 0

        for i in range(len(s)):
            # Expected character in alternating pattern "010101..."
            if s[i] != str(i % 2):
                count1 += 1
            # Expected character in alternating pattern "101010..."
            if s[i] != str((i + 1) % 2):
                count2 += 1

        # Return the minimum of the two possible patterns
        return min(count1, count2)


# o(n) runtime and constant time space unless you count the 2 variables
# the idea is that there are only two possible answers. One that starts with 1 and one that starts with 0
# we keep count of changes for string that starts with an expected 1 or 0
# we do two if checks while iterating, at each element we will keep count if we need to change it or not based on expected
# 1010101 or 0101010 pattern strings
# we then return the minimum of the counts


# Explanation:
# Two Patterns: We consider two patterns:
# "010101..."
# "101010..."
# Count Mismatches: For each position i, we check if the character matches the expected character for each pattern.
# Return the Minimum Count: We return the smaller count between the two possible patterns. This ensures the minimum number of operations required to convert the string to an alternating pattern.


# 1758. Minimum Changes To Make Alternating Binary String
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

 

# Example 1:

# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.
# Example 2:

# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.
# Example 3:

# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".
 

# Constraints:

# 1 <= s.length <= 104
# s[i] is either '0' or '1'.

# https://pythontutor.com/render.html#code=class%20Solution%3A%0A%20%20%20%20def%20minOperations%28self,%20s%3A%20str%29%20-%3E%20int%3A%0A%20%20%20%20%20%20%20%20count1,%20count2%20%3D%200,%200%0A%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28s%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20Expected%20character%20in%20alternating%20pattern%20%22010101...%22%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20s%5Bi%5D%20!%3D%20str%28i%20%25%202%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20count1%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20Expected%20character%20in%20alternating%20pattern%20%22101010...%22%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20s%5Bi%5D%20!%3D%20str%28%28i%20%2B%201%29%20%25%202%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20count2%20%2B%3D%201%0A%0A%20%20%20%20%20%20%20%20%23%20Return%20the%20minimum%20of%20the%20two%20possible%20patterns%0A%20%20%20%20%20%20%20%20return%20min%28count1,%20count2%29%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.minOperations%28%220100%22%29&cumulative=false&curInstr=3&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false