class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        l ,r = 0, 0
        count = 0

        while r <= len(nums) -1:
            if r == len(nums) - 1 and nums[r] == 0:
                if nums[r] == 0:
                    count += 1
                    total += (count * (count + 1)) // 2

            if nums[r] != 0:
                l = r
                if count != 0:
                    total += (count * (count + 1)) // 2
                    count = 0
                
            else:
                count +=1
             
            r += 1
        return total
    
# my solution 0(n) time and space one pass and counts variables
# my algorithm is to find lengths of subarrays of 0's and to keep that length
# when the subarray ends i use the sum of natural numbers formulas with that length as X and add to a total
# i return that total after im done
# i had to throw boundary checks at the end because i ended once right pointer got to the end but didnt update total if the end was a 0
# while r in bounds
# i will first check if nums[r] is a zero
#       if it is then i will increase count by 1 and add to total
# this takes care of end of nums list 0's
# if nums[r] isnt a zero then i will move left to right pointer
#   then i will check if count isnt 0
#       if it isnt i will perform the sum of natty numbers formula with count as X and then reset count to 0
# else i found a zero so i will increase count
# i will keep moving right pointer throughout each loop
# return count
# runtime 97ms and only beats 5.71% and memory is 27.58mb and only beats 5.40%


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i, res = 0, 0
        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i] == 0:
                count +=1
                res += count
                i += 1

            i += 1
        return res
    
# neetcodes more optimal solution
# algo is some mathy stuff where each subarray that increases in length adds length + 1 to the total subarrays in it
#  subarray of 3 0's will be previous length of 00 plus 3....so at two zeroes it was 3 so we add the current length of 3 to it
# subarray length examples
#  1 = 1
#  2 = 1 + 2
# 3 = 3 + 3
# 4 = 6(prev) + 4(current length)
# 5 = 10(prev) + 5(cur)
# 6 = 15(previous subarrays) + 6(current length)
# while i in bounds
# set count to 0...if we end a subarray and continue on we will have a fresh start
# then while i in bounds and we are at a 0
#  we increase count + 1 then add that total and then increase i +=1
# we increase i outside of the inner while loop to keep the iteration going
# return res
        
    # 2348. Number of Zero-Filled Subarrays
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
# Example 2:

# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
# Example 3:

# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.