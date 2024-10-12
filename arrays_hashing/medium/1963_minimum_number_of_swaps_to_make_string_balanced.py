class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        maxClose = 0
        for c in s:
            if c == "[":
                count -=1
            else:
                count += 1
            maxClose = max(count, maxClose)
        return (maxClose + 1) // 2
        


# o(n) one pass solution constant space
# keep running count of open vs closed parenthesis as count vs a maxcount. maxcount is the highest the count gets positively counting
# closed parentheses
# we iterate through the string and if its an opening parenthesis we subtract 1 else we add 1
# at the end of each iteration we take the max of current maxCount or current count
# this ensures we have the highest number of difference between open and close
# we need the highest closing count so we can +1 and remainder division by 2 after and return the result
# we add 1 first because it theres an odd number then we round up
# we divide by 2 because every swap fixes 2 brackets




# Why do we divide by 2?
# Each swap allows us to exchange an unmatched closing bracket (]) with an unmatched opening bracket ([).
# One swap fixes two brackets—one opening and one closing.
# So, to correct a certain number of unmatched brackets, the number of swaps needed is half the number of unmatched closing brackets (maxClose), because each swap addresses both an opening and a closing bracket.
# Thus, we divide by 2 because each swap corrects 2 brackets (1 closing bracket and 1 opening bracket).

# Why do we add 1?
# The addition of 1 is used to handle odd numbers of unmatched closing brackets.
# For example, if maxClose is 3, we have an odd number of unmatched closing brackets. In this case, (3 + 1) // 2 ensures that we round up.
# Adding 1 ensures that any odd number of unmatched brackets rounds up correctly, giving us the minimum number of swaps needed.
# Example with an odd number of unmatched closing brackets:
# Consider a string where there are 3 extra closing brackets at one point (maxClose = 3). We know that:

# Each swap fixes 2 brackets.
# But with 3 unmatched brackets, we can't perfectly divide by 2 (since we need to swap 1 more bracket than 2).
# In this case, adding 1 ensures that we account for the extra unmatched bracket, making the formula (3 + 1) // 2 = 2, meaning we need 2 swaps.
# Example with an even number of unmatched closing brackets:
# If there are 4 unmatched closing brackets (maxClose = 4):

# The formula (4 + 1) // 2 = 2 correctly gives us 2 swaps.
# Since each swap fixes 2 brackets, 2 swaps fix all 4 unmatched brackets.
# Summary:
# Dividing by 2 handles the fact that each swap fixes 2 brackets.
# Adding 1 handles cases where the number of unmatched brackets is odd, ensuring the number of swaps is rounded up to the correct amount.

# 1963. Minimum Number of Swaps to Make the String Balanced
# Medium
# Topics
# Companies
# Hint
# You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

# A string is called balanced if and only if:

# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.
# You may swap the brackets at any two indices any number of times.

# Return the minimum number of swaps to make s balanced.

 

# Example 1:

# Input: s = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index 3.
# The resulting string is "[[]]".
# Example 2:

# Input: s = "]]][[["
# Output: 2
# Explanation: You can do the following to make the string balanced:
# - Swap index 0 with index 4. s = "[]][][".
# - Swap index 1 with index 5. s = "[[][]]".
# The resulting string is "[[][]]".
# Example 3:

# Input: s = "[]"
# Output: 0
# Explanation: The string is already balanced.
 

# Constraints:

# n == s.length
# 2 <= n <= 106
# n is even.
# s[i] is either '[' or ']'.
# The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.