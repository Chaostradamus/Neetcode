class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      changes = 0
      for i in range(len(nums)):
        if nums[i+1] and nums[i+1] != nums[i] +1:
          nums[i+1] = nums[i] +1
          changes += 1
          if changes > 0:
            return nums[i:i+2]
          

# my algo works with numbers that ascend but not when they descend in value


# second try..answer is wrong still because it can be ascending descending and missing numbers..what the fuck
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      size = len(nums)
      
      count = {}
      for i in range(size):
        count[i+1] = 0
      for n in nums:
        count[n] = count.get(n, 0) +1
      for c in count:
        if count[c] == 2:
          if count.get(c-1) == 0:
            return [c, c-1]
          else:
            return [c, c+1]


          
# on my second try it takes care of descending order
# we populate a hashmap of size len(nums)
# we iterate through thr hashmap until we find the countn thats = 2 and we check if the above or below character count is empty
# if either is empty we return that character and the empty one
# we use the .get method to ensure no errors when we find the 0
# on second check this only works when numbers are adjacent and ascending so nums such as 3,1 wont work with my algo



# real solution from neetcode

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      res =[0,0]
      count = Counter(nums)

      for i in range(1, len(nums) + 1):
        if count[i] == 0:
          res[1] = i
        if count[i] == 2:
          res[0] = i
      return res 

# WE ARE FINDING THE MDUPLICATE AND MISSING NUMBER..IF NO DUPLICATE IT WILL RETURN 0
# MAY NOT BE A MISSING OR A DUPLICATE
# this keeps a result array for duplicate number and missing number
# populate a count of nums
# iterate through from 1 to len of nums + 1 (this will start at 1 like the question states and go up the the len of nums...the +1 is for indexing)
# this ensure we go from 1 to n where n is the amount of numbers
# if the count = 2 at that element, we know its the duplicate so we set res[0] to i
# if the count = 0 at that element,  we know its the missing so we set res[1] to i

# UPDATE...THE ABOVE CODE ONLY HANDLES ONE MISSING VALUE

# for the above on nums[3,4], isnt 2 also missing?
# ChatGPT said:
# ChatGPT
# Yes, you are correct. For the array nums = [3, 4]:

# The array should ideally contain all numbers from 1 to 2 (since len(nums) = 2).
# Given nums = [3, 4], the missing numbers are indeed 1 and 2, because these numbers are not present in the array.
# Issue with the Code:
# The current code might not correctly handle scenarios where multiple numbers are missing. It is designed to handle one missing and one duplicated number, but in this case, it would only return one missing number because the algorithm assumes only one missing and one duplicated number.

# Updated Code to Handle Multiple Missing Numbers:
# To properly handle scenarios where multiple numbers are missing, you would need to adjust the approach. Here's an updated approach that can handle such cases:

# python
# Copy code
# from collections import Counter
# from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        size = len(nums)
        count = Counter(nums)
        
        duplicate = missing = None
        
        # Track the actual numbers present in the list
        for i in range(1, size + 1):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                if missing is None:
                    missing = i
                else:
                    missing = i  # Update missing if necessary
        
        return [duplicate, missing]

# Example usage:
# solution = Solution()
# print(solution.findErrorNums([3, 4]))  # Output: [None, [1, 2]]
# Explanation:
# Count Frequencies:

# Use Counter(nums) to get the frequency of each number.
# Identify Duplicates and Missing Numbers:

# Iterate through the range 1 to size and:
# Set duplicate if a number has a count of 2.
# Set missing if a number is missing (count is 0).
# Final Output for [3, 4]:
# The code will identify that 1 and 2 are missing, but in this case, it would only return [None, 1] because of the limitations of the original code.
# Summary:
# The original code does not fully handle multiple missing numbers and can give incomplete results. The updated code should handle such scenarios better by providing a more accurate result.


# UPDATED FINAL CODE THAT HANDLES ALL MISSING NUMBERS

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        size = len(nums)
        count = Counter(nums)
        
        duplicate = None
        missing = []

        # Check for missing and duplicated numbers
        for i in range(1, size + 1):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing.append(i)

        return [duplicate, missing]
    
# this takes the same approach as the others, except we set duplicate and missing variables from the start
# we set missing to an array, we can also do this for duplicates if we want to check for missing multiple duplicates
# we take size of array and set as variable
# we take a count of nums
# we iterate through count at each number 1-n
# if the counts value is a 2, its the duplicate and we set duplicate to i
# there is only one duplicate in the nums array
# if the count's value is a 0, we append to the missing array
# we return [duplicate, missing] at the end
# original question has a lot of unmentioned things such as how many or which missing numbers
# test cases also dont always start at 1



      # res = [0,0]
      # for n in nums:
      #   n = abs(n)
      #   nums[n-1] = -nums[n-1]
      #   if nums[n-1] > 0:
      #     res[0] = n
      # for i, n in enumerate(nums):
      #   if n > 0 and i + 1 != res[0]:
      #     res[1]= i + 1
      #     return res


# 645. Set Mismatch
# Attempted
# Easy
# Topics
# Companies
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104



# https://pythontutor.com/render.html#code=from%20typing%20import%20List%0Afrom%20collections%20import%20Counter%0A%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20findErrorNums%28self,%20nums%3A%20List%5Bint%5D%29%20-%3E%20List%5Bint%5D%3A%0A%20%20%20%20%20%20%20%20size%20%3D%20len%28nums%29%0A%20%20%20%20%20%20%20%20count%20%3D%20Counter%28nums%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20duplicate%20%3D%20None%0A%20%20%20%20%20%20%20%20missing%20%3D%20%5B%5D%0A%0A%20%20%20%20%20%20%20%20%23%20Check%20for%20missing%20and%20duplicated%20numbers%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%281,%20size%20%2B%201%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20count%5Bi%5D%20%3D%3D%202%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20duplicate%20%3D%20i%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20count%5Bi%5D%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20missing.append%28i%29%0A%0A%20%20%20%20%20%20%20%20return%20%5Bduplicate,%20missing%5D%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.findErrorNums%28%5B3,4%5D%29&cumulative=false&curInstr=20&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false