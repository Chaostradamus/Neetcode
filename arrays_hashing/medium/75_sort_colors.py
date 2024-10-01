class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numCount = {0:0, 1:0, 2:0}
        for n in nums:
          if n in numCount:
            numCount[n] += 1
          else:
            numCount[n] = 1
        i = 0

        if len(nums) <= 1:
          return

        for n in numCount:
          b = numCount[n]
          while b > 0:
            nums[i] = n
            i +=1
            b -= 1


# 0(n) space and time because of hashmap and one pass trough nums array
# populate a hard coded hashpmap that already contains 0 to 3 with nums where element is key and value = count
# for every element in a now sorted numCount hashmap
# keep an i for len  and boundary check
# keep a count for every element
#  change nums[i] to current element and decrement count and increase i pointer
# at the end every element with a count will be used to fill in the current position of nums while the count decrements


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) -1
        i = 0

        def swap(i, j):
          temp = nums[i]
          nums[i] = nums[j]
          nums[j] = temp

        while i <= r:
          if nums[i] == 0:
            swap(l, i)
            l += 1
          elif nums[i] == 2:
            swap(i, r)
            r -= 1
            i -= 1
          i += 1

# neetcode o(n)  one pass solution...all others would be two pass to create another data structure or nlogN cause of some sort of sorting function
# we hold 3 pointers..a left right and an i
# we create a swap function to swap in place and use a the helper function to reduce code
# while i is <= r that means we are not passed the sorted backup yet
# if current element is a 0 we swap left and i and increase L
# if current position is a 2, we swap i with right element and decrease r and i
# no matter what after the if checks we will increase i

# the thinking behind how to move the pointers is this
# l keeps track of whwre to put 0's and right keeps track of where to put 2's
# we dont want to move i if we find a 2 because then we may find more 0's and willhave no way to know where to put it 
# i think
# the big thing is misplacing 2's and 1's if we move them i after everything so we dont move i when we find a 2

# 75. Sort Colors
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.


https://pythontutor.com/render.html#code=from%20typing%20import%20List%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20sortColors%28self,%20nums%3A%20List%5Bint%5D%29%20-%3E%20None%3A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20l,%20r%20%3D%200,%20len%28nums%29%20-1%0A%20%20%20%20%20%20%20%20i%20%3D%200%0A%0A%20%20%20%20%20%20%20%20def%20swap%28i,%20j%29%3A%0A%20%20%20%20%20%20%20%20%20%20temp%20%3D%20nums%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20nums%5Bi%5D%20%3D%20nums%5Bj%5D%0A%20%20%20%20%20%20%20%20%20%20nums%5Bj%5D%20%3D%20temp%0A%0A%20%20%20%20%20%20%20%20while%20i%20%3C%3D%20r%3A%0A%20%20%20%20%20%20%20%20%20%20if%20nums%5Bi%5D%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20swap%28l,%20i%29%0A%20%20%20%20%20%20%20%20%20%20%20%20l%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20elif%20nums%5Bi%5D%20%3D%3D%202%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20swap%28i,%20r%29%0A%20%20%20%20%20%20%20%20%20%20%20%20r%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.sortColors%28%5B2,0,2,1,1,0%5D%29&cumulative=false&curInstr=61&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false