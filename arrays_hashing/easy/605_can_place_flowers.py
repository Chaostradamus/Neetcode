class Solution:
    
      def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       # Solution with O(n) space complexity
        f = [0] + flowerbed + [0]
       
        for i in range(1, len(f) - 1):  # skip first & last
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
               f[i] = 1
               n -= 1
        return n <= 0
      


# we add empty spots to the beginning and end of the array
# we iterate from the 1st real spot in the array to the last real spot
# if current spot and the prev and next spots are empty
# we place a flower there and decrease N by 1
# return statement of n <= 0 means we return true if n = 0 else False 





# 605. Can Place Flowers
# Easy
# Topics
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false