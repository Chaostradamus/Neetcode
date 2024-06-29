class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
      max_right = -1
      for i in range(len(arr) -1, -1, -1):
        current = arr[i]
        arr[i] = max_right
        max_right = max(current, max_right)
      return arr

# i originally used two for loops..one to traverse the array and on nested to traverse fro ma given upper element to find and hold a max
# but that was o of n squared runtime
# hold max right as -1 to start
# traverse array backwards 
# first set current  to current element to hold it
# set current element to max right..on first iteration is will be -1
# then we take the max of current and max_right
# return array at the end


# https://pythontutor.com/render.html#code=from%20typing%20import%20List%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20replaceElements%28self,%20arr%3A%20List%5Bint%5D%29%20-%3E%20List%5Bint%5D%3A%0A%20%20%20%20%20%20%20%20max_right%20%3D%20-1%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28arr%29%20-%201,%20-1,%20-1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20current%20%3D%20arr%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20arr%5Bi%5D%20%3D%20max_right%0A%20%20%20%20%20%20%20%20%20%20%20%20max_right%20%3D%20max%28max_right,%20current%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20arr%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.replaceElements%28%5B17,18,5,4,6,1%5D%29&cumulative=false&curInstr=28&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false
# 1299. Replace Elements with Greatest Element on Right Side
# Easy
# Topics
# Companies
# Hint
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

 

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:

# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.
 