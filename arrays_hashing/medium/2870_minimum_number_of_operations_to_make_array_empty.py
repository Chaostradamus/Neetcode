class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = {}
        steps = 0
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, n in count.items():
            
            
            while n > 0:
                if n % 3 == 0:          # If n is divisible by 3, subtract 3
                    n -= 3
                elif n >= 2:            # Otherwise, subtract 2 if possible
                    n -= 2
                else:
                    return -1
                steps += 1        # If no moves are possible to make n zero, return False
        return steps
    
# my algo is m*n one pass and hashmap lookup and o(n) space
# i populate a hashmap with nums values and then i iterate through each num element and count in the hashmap
# i perform decrements by 3 and 2 until it reaches 0...if it doesnt reach zero at any point i retuen -1
# my decrementing algorithm is to minus by 3 when the count is divisible by 3 with no remainder
# else i will decrement by 2 is the number is 2 or greater
# every decrement will add a +=1 1 to total steps taken
# i will return steps at the end

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        count = Counter(nums)

        for n, c in count.items():
            if c == 1:
                return -1
            res += ceil(c/3)
        return res


# neetcode mathy solution o(n) time and space also
# populate hashmap
# mathy algo is that you divide by 3 and then add 1 if its not divisible by 3 hence the ceiling function rounding up
# for example 100...we do 100 divided by 3




# 2870. Minimum Number of Operations to Make Array Empty
# Solved
# Medium
# Topics
# Companies
# You are given a 0-indexed array nums consisting of positive integers.

# There are two types of operations that you can apply on the array any number of times:

# Choose two elements with equal values and delete them from the array.
# Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

 

# Example 1:

# Input: nums = [2,3,3,2,2,4,2,3,4]
# Output: 4
# Explanation: We can apply the following operations to make the array empty:
# - Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
# - Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
# - Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
# - Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
# It can be shown that we cannot make the array empty in less than 4 operations.
# Example 2:

# Input: nums = [2,1,2,2,3,3]
# Output: -1
# Explanation: It is impossible to empty the array.