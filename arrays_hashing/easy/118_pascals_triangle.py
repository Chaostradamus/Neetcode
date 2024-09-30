class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      res =[[1]]

      for i in range(numRows -1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) +1):
          row.append(temp[j] + temp[j+1])
        res.append(row)
      return res
    
    # o(N^2) runtime and space because n rumber of rows and space kept where it get
    # initialize res first with [1] because it will always be a 1 first row
    # we then iterate through numrows -1 amount of times because we already made the first row
    # we hold a temp array with dummy 0's in the front and back of it and a new row that we will create and append to res
    # we inner for loop the length of the last row +1 amount of times because each new row is 1 element bigger
    # we have a 2 element sliding window....we add temp array at [j] and [j+1] to the row and append row to res at the end


# 118. Pascal's Triangle
# Easy
# Topics
# Companies
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 