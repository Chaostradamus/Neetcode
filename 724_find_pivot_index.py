class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      total = sum(nums)

      left = 0

      for i in range(len(nums)):
        right = total - nums[i] - left
        if left == right:
          return i
        left += nums[i]
      return -1
    
# we sum up the total of nums because its constant and we can check off that
# set left to 0 to keep a count for the left side up the that point
#  iterate through nums and calculate right as the total left and current elemtn of nums
#  if left and right are matched up then we found the pivot index
#  if not we add current element to left count and continue
#  return -1 if we dont find the pivot index
#  o(n) because we just ierate through everything once...brute force with be o(n)^2


# 724. Find Pivot Index
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

 

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
# Example 2:

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Example 3:

# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0


# https://pythontutor.com/render.html#code=from%20typing%20import%20List%0Afrom%20collections%20import%20defaultdict%0A%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20pivotIndex%28self,%20nums%3A%20List%5Bint%5D%29%20-%3E%20int%3A%0A%20%20%20%20%20%20%20%20total%20%3D%20sum%28nums%29%20%20%23%20O%28n%29%0A%0A%20%20%20%20%20%20%20%20leftSum%20%3D%200%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28nums%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20rightSum%20%3D%20total%20-%20nums%5Bi%5D%20-%20leftSum%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20leftSum%20%3D%3D%20rightSum%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20i%0A%20%20%20%20%20%20%20%20%20%20%20%20leftSum%20%2B%3D%20nums%5Bi%5D%0A%20%20%20%20%20%20%20%20return%20-1%0A%20%20%20%20%20%20%0A%0Ab%20%3D%20Solution%28%29%0Ab.%20pivotIndex%28%5B1,7,3,6,5,6%5D%29&cumulative=false&curInstr=16&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false