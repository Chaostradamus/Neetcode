class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key = cmp_to_key(compare))

        return str(int("".join(nums)))


# so the important thing in the largest number question is that we turn everything to strings,
#  then we pass in everything to sorted. our compare function returns the larger number out of combined n1 and n2 on evenutally everything
#  and returns it sorted to us?



# 179. Largest Number
# Medium
# Topics
# Companies
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109