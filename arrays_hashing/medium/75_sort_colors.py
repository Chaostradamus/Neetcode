class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numCount = {0:0, 1:0, 2:0}
        for n in nums:
          if n in numCount:
            numCount[n] += 1
          else:
            numCount[n] = 1
        i = 0

        if len(nums) <= 1:
          return

        for n in numCount:
          b = numCount[n]
          while b > 0:
            nums[i] = n
            i +=1
            b -= 1


# 0(n) space and time because of hashmap and one pass trough nums array
# populate a hard coded hashpmap that already contains 0 to 3 with nums where element is key and value = count
# for every element in a now sorted numCount hashmap
# keep an i for len  and boundary check
# keep a count for every element
#  change nums[i] to current element and decrement count and increase i pointer
# at the end every element with a count will be used to fill in the current position of nums while the count decrements


# 75. Sort Colors
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.