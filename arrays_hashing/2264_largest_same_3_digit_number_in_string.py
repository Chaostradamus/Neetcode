class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        res = "0"

        for i in range(len(nums)-2):
          if nums[i] == nums[i+1] == nums[i+2]:
            res = max(res, nums[i:i+3])
        
        return "" if res == "0" else res

# o(n) runtime and constant time space
# we set a result variable to string "0" 
# we do this instead of a triple digit 0 because we want to differentiate between finding nothing and actual 000's
# we have a sliding window of size 3 and iterate through the array until the 2nd to last string or else we will be out of bounds
# if we find a valid 3 digit string then we take the max of current res and the current window as new res
# we will return "" blank if none are found by check if res still equals 0
# else we will return res


# so lexicographically, is 22 larger or is 111
# ChatGPT said:
# ChatGPT
# In lexicographical (dictionary) order, "22" is considered larger than "111".

# Why?
# Lexicographical comparison is done character by character from left to right.
# The first character of "22" is "2", and the first character of "111" is "1".
# Since "2" is greater than "1" (just like in a dictionary where words starting with later letters come after those starting with earlier letters), "22" is considered greater than "111".
# Examples:
# "3" is greater than "20" because "3" comes after "2".
# "abc" is greater than "ab" because it is longer and the first two characters are identical.
# "22" is greater than "111" because "2" is greater than "1".
# So in your case, "22" would be considered larger than "111" when comparing lexicographically.

# 2264. Largest 3-Same-Digit Number in String
# Easy
# Topics
# Companies
# Hint
# You are given a string num representing a large integer. An integer is good if it meets the following conditions:

# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.

# Note:

# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.
 

# Example 1:

# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".
# Example 2:

# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.
# Example 3:

# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
 

# Constraints:

# 3 <= num.length <= 1000
# num only consists of digits.