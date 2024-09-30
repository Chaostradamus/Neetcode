class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      numsMap = { n:i for i, n in enumerate(nums1) }
      res = [-1] * len(nums1)

      stack = []
      for i in range(len(nums2)):
        cur = nums2[i]

        while stack and cur > stack[-1]:
          val = stack.pop()
          idx = numsMap[val]
          res[idx] = cur

        if cur in numsMap:
          stack.append(cur)
      return res
    

# o(m+n) runtime because we go through each array once
# o(m) space because of stack
# first we create hashmap with element as key and index value
# create res array with all -1's
# create a stack
# iterate through nums2 
# set current to current element we are at in nums2
# if the stack isnt empty and current is larger than top of stack (this means we found a larger element and we must do something)
# val = popped val from top of stack
# index = hashmap[val] (this gives us the index of the value)
# res at the index set to val ( this gives us next largest element of current element)
# if current element from nums2 is in numsHashmap, we can add to stack (this means we only add elements from nums2 if theyre in nums1 to stack)
# return res


# 496. Next Greater Element I
# Easy
# Topics
# Companies
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

# https://pythontutor.com/visualize.html#code=from%20typing%20import%20List%0A%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20nextGreaterElement%28self,%20nums1%3A%20List%5Bint%5D,%20nums2%3A%20List%5Bint%5D%29%20-%3E%20List%5Bint%5D%3A%0A%0A%20%20%20%20%20%20%20%20%23%20O%20%28n%20%2B%20m%29%0A%20%20%20%20%20%20%20%20nums1Idx%20%3D%20%7B%20n%3Ai%20for%20i,%20n%20in%20enumerate%28nums1%29%20%7D%0A%20%20%20%20%20%20%20%20res%20%3D%20%5B-1%5D%20*%20len%28nums1%29%0A%0A%20%20%20%20%20%20%20%20stack%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28nums2%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20cur%20%3D%20nums2%5Bi%5D%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20while%20stack%20exists%20and%20current%20is%20greater%20than%20the%20top%20of%20the%20stack%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20stack%20and%20cur%20%3E%20stack%5B-1%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20val%20%3D%20stack.pop%28%29%20%23%20take%20top%20val%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20idx%20%3D%20nums1Idx%5Bval%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20res%5Bidx%5D%20%3D%20cur%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20cur%20in%20nums1Idx%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20stack.append%28cur%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20res%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.nextGreaterElement%28%5B4,1,2%5D,%5B1,3,4,2%5D%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false