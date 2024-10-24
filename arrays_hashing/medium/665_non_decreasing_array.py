class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums) -1):
            if nums[i] <= nums[i+1]:
                continue
            if changed:
                return False
            if i ==0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            changed = True
        return True
    

# o(n) space and o(1) time
# we first keep a boolean flag and then iterate in pairs by doing range len of nums -1 to not do the last element
# we check if nums[i] is greater than nums[i+1]...if it is then we continue the iteration
# if the first if check doesnt go then we check if we have previous modification then return false if we did have a mod
# then if that passes we can finally check how we will mod nums
#      first check if we are at the first element ...include this in the first check because we will either be at first element
# or we will be at changing i to nums[i+1] anyway
# the first check will be if i == o or if element after i is greater/equal to element before i
#    if this is the case we can safely change nums[i] to nums[i+1]
# else we will do the opposite and change nums[i+1] to nums[i]
# this is because we do not want to break the order for example 3,4,2
# if we are at 4 we want to check  the 2 and 3 with each other...since 2 is smaller we change 2 to 4
# if the reverse situation was true then we change 4 to whatever i+1 is

# Key Reasoning
# The goal of the algorithm is not only to achieve a non-decreasing sequence but to ensure that only one modification can achieve that goal.
# The modification to change 10 to 8 ensures that the original values are adjusted in a way that resolves the violation directly and allows for a future possible adjustment without further violations.
# If you had opted for [7, 10, 10], you might be able to maintain a non-decreasing order momentarily, but it introduces the possibility of further violations if more elements were present, making it less robust to additional changes.

# Summary
# Valid Modification: Changing to [7, 8, 8] resolves the violation while maintaining the original number's context and allows for the next steps in the array to remain valid.
# Invalid Modification: Changing to [7, 10, 10] does not effectively resolve the violation created by 10 > 8 in a way that could allow for other modifications later.
# Therefore, the choice to set nums[i] to nums[i+1] in this instance leads to a more stable solution under the constraints of the algorithm.



# 665. Non-decreasing Array
# Medium
# Topics
# Companies
# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# -105 <= nums[i] <= 105