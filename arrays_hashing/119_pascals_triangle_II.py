class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
      res = [[1]]

      for i in range(rowIndex):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1])+ 1):
          row.append(temp[j] + temp[j+1])
        res.append(row)
      return res[-1]
    
# my solution o(n^2) time and space
# we connstruct pascals triangle by first initializing the first row. this will take care of indexing also
# since if we are looking for the 3rd row the first row is skipped but the range function is 0th index so the count will be the same
# ie 3rd row would normally return the 2nd row but since we skipped the first row due to initializing, we will get the correct row
# create a temporary row with 0's in front and back to fix index out of bound issues 
# create an empty row
# we loop through the length of the previous row +1 amount of times because each succeeding row is +1 bigger
# we add to row temp[j] and temp[j+1] and this will fill in the row 
# then we append it
# at the end we return the last row we filled and this will be correct because we took rowInde as the amount of times we would loop through
# would be the correct amount of rows we would be building

# neetcode updates row in place and returns after done iterating
# this saves us space and makes space o(n) instead of n^2
# he creates a new row of all 1's the length of prev row + 1
# iterates in place while updating the values and sets as new res
# eventually returns this result


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)  # Initialize the row with 1s
        
        # Update the row from the second last element to the first for each i
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]  # Update the current element
        
        return row

# chatgpt solution
# also does everything in place but cuts out some extra space
# this solution creates an array with all 1's the size of row index+ 1 to take care of the 0th indexing
# outer for loop iterates from 1 index row to rowindex
# innder for loop will run from i down to zero and update values in reverse
# ultimately returning res


# 119. Pascal's Triangle II
# Easy
# Topics
# Companies
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33
 

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?