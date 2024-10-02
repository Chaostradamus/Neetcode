class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
      gaps = {0:0}
      for r in wall:
        total = 0
        for b in r[:-1]:
          total += b
          gaps[total] = 1 + gaps.get(total, 0)
      
      return len(wall) - max(gaps.values())


# o(N) time and space
# the question is a 2d array where it simulates a brick wall and the end of each bricks length is a gap
# for example is a row is 2, 3, 1...then the end of the first brick of length 2 is a gap...the end of the next
# brick will be another gap and so on. the edges dont count
# we create a hashmap where key is the length where theres a gap, and value is the amount of gaps at that length in each row
# we iterate over every row and then brick by brick like any 2d array
# we set a total to keep track of current length..we add brick by brick to the total and after each brick
# after a brick is added we use that total and increment its gap count in the hashmap
# after the hashmap is filled we will know which length has the most gaps in between bricks
# we return the total number of rows minus the length that has the most gaps


# 554. Brick Wall
# Medium
# Topics
# Companies
# There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

# Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

 

# Example 1:


# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
# Example 2:

# Input: wall = [[1],[1],[1]]
# Output: 3
 

# Constraints:

# n == wall.length
# 1 <= n <= 104
# 1 <= wall[i].length <= 104
# 1 <= sum(wall[i].length) <= 2 * 104
# sum(wall[i]) is the same for each row i.
# 1 <= wall[i][j] <= 231 - 1