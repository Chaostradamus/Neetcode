class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
      count = {}

      for w, h, in rectangles:
        count[w / h] = 1 + count.get(w /h, 0)
      
      res = 0
      for c in count.values():
        if c > 1:
          res += (c * (c-1)) //2
      return res
# neetcode solution
# create hashmap and map ratio as the key and count as the value
# iterate through the hashmaps values and if the count is greater than 1 we do math
#  we check if its greater than 1 because if only one rectangle has that ratio then we cant make pairs+


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
      ratio = {}
      count = 0

      for n in rectangles:
        key = tuple(n)
        if n[1] != 0:
          value = n[0] / n[1]
          ratio[key] = value

      keys = list(ratio.keys())

      for i in range(len(keys)- 1):
        key = keys[i]
        val = ratio[key]
        j = i+ 1
        while j < len(keys):
          key2 = keys[j]
          val2 = ratio[key2]
          if val == val2:
            count += 1
          j += 1
      return count


# my solution that only passed about 8/60 test cases
# put the rectangles into a hashamp where the dimensions are keys and the ratio are values
# convert the hashmap back into a list to make it iterable and to extract an index
# iterate through keys and extract the index to extract the value out of ratio hashmap
# create j variable that acts as a pointer that slides forward
# use j and extract key and ratio value just like before and compare the values of i and j
# increate count if they match and increase j 
# return j


# 2001. Number of Pairs of Interchangeable Rectangles
# Medium
# Topics
# Companies
# Hint
# You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

# Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

# Return the number of pairs of interchangeable rectangles in rectangles.

 

# Example 1:

# Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
# Output: 6
# Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
# - Rectangle 0 with rectangle 1: 4/8 == 3/6.
# - Rectangle 0 with rectangle 2: 4/8 == 10/20.
# - Rectangle 0 with rectangle 3: 4/8 == 15/30.
# - Rectangle 1 with rectangle 2: 3/6 == 10/20.
# - Rectangle 1 with rectangle 3: 3/6 == 15/30.
# - Rectangle 2 with rectangle 3: 10/20 == 15/30.
# Example 2:

# Input: rectangles = [[4,5],[7,8]]
# Output: 0
# Explanation: There are no interchangeable pairs of rectangles.