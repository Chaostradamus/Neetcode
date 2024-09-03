class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      seen = set()
      res = []
      for n in nums1:
        seen.add(n)
      for n in nums2:
        if n in seen:
          res.append(n)
          seen.remove(n)
      return res
    

# use a hashset for first array
# while iterating through nums2 comparing to seen hashset
# if nums2 current element is in seen hashset, add it to res array but also remove it from seen 
# this prevents us from adding duplicates to res array since we remove it from the seen hashmap
# this is  o(n) time and space. technically 2n cause we go through both arrays 



# 349. Intersection of Two Arrays
# Easy
# Topics
# Companies
# Given two integer arrays nums1 and nums2, return an array of their 
# intersection
# . Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000