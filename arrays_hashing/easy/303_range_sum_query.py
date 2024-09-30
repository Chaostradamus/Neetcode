class NumArray:

    def __init__(self, nums: List[int]):
      self.prefix = []
      cur = 0
      for n in nums:
        cur += n
        self.prefix.append(cur)
        

    def sumRange(self, left: int, right: int) -> int:

      rightS = self.prefix[right]
      leftS = self.prefix[left-1] if left > 0 else 0
      return rightS - leftS
        
# 303. Range Sum Query - Immutable
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

# constructor is o(n) and lookup is constant time
# make constructor with prefix array
# loop through nums and fill up prefix array 

#  rangeSum
# set rightSum and leftSum accordingly
# right as prefix[right] and left as prefix[left -1] because we need everything up to that point on the left so we -1 that side
# alsohave to check if left is greater than 0 to keep it in bounds
# return rightSUm - leftSum 