# neetcode

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l ,m,  r):
          left = arr[l:m+1]
          right = arr[m+1:r+1]
          i = l
          j,k = 0, 0
          while j < len(left) and k < len(right):
            if left[j] <= right[k]:
              arr[i] = left[j]
              j += 1
            else:
              arr[i] = right[k]
              k += 1
            i +=1
          while j < len(left):
            arr[i] = left[j]
            i +=1
            j +=1
          while k < len(right):
            arr[i] = right[k]
            i += 1
            k += 1
        def mergeSort(arr, l, r):
          if l ==  r:
            return arr
            
          m = (l + r) // 2
          mergeSort(arr, l, m)
          mergeSort(arr, m+1, r)
          merge(arr, l ,m, r)
          return arr
     

        return mergeSort(nums, 0, len(nums) -1)



from typing import List



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge function to combine two sorted halves of the array
        def merge(arr, L, M, R):
            # Create temporary arrays for the left and right halves
            left = arr[L:M+1]  # Left subarray from L to M (inclusive)
            right = arr[M+1:R+1]  # Right subarray from M+1 to R (inclusive)
            
            # Indices to iterate through left, right, and the main array
            i = L  # Starting index in the main array to place sorted elements
            j, k = 0, 0  # j for left subarray, k for right subarray
            
            # Merge elements from both subarrays in sorted order
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:  # If the element in left is smaller
                    arr[i] = left[j]     # Place it in the main array
                    j += 1               # Move to the next element in the left subarray
                else:  # If the element in right is smaller
                    arr[i] = right[k]    # Place it in the main array
                    k += 1               # Move to the next element in the right subarray
                i += 1                   # Move to the next position in the main array
            
            # Copy any remaining elements from the left subarray (if any)
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            
            # Copy any remaining elements from the right subarray (if any)
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        # Merge Sort function to recursively sort the array
        def mergeSort(arr, l, r):
            if l < r:  # Recursion continues as long as the subarray has more than one element
                # Find the middle point of the current subarray
                m = (l + r) // 2  # Divide the array into two halves
                
                # Recursively sort the left half (from l to m)
                mergeSort(arr, l, m)
                
                # Recursively sort the right half (from m+1 to r)
                mergeSort(arr, m + 1, r)
                
                # Merge the sorted left and right halves
                merge(arr, l, m, r)
            
            return arr  # Return the sorted array once the entire array has been processed

        # Initial call to mergeSort with the full array (from index 0 to len(nums)-1)
        return mergeSort(nums, 0, len(nums) - 1)

# O logN runtime because we split into smaller sublits and rebuild back up and constant space because we dont use any extra memory
# the main points are two define a merging function and then a main function
# call mergeSort on the original array 
# check if its valid and then find the midpoint
# call mergeSort on the left side from left to mid
# call mergesort on right side from mid to right
# then merge
# this will break each side down to one element and return back up while sorting smaller sublists until
# eventually we get back up to two filly sorted halves before we sort those two halves into the final version
# divide and conquer

# merging function takes the left right and middle
# sets the array from passedin L so as to not confuse..we dont sort from the L of the entire array
# we sort from the left of the subarray so we pass in L instead of 0
# when defining left vs right when passing in the subarrays
# we set 3 pointers, one for the left and right array and one for the main array
# while the lengths of both the left and right pointer are in bounds we check which value at the current index
# at both arrays are smaller and set the arr[i] to that value
# we increase i and the left or right pointers depending on which one we just used
# sometimes one subarray runs out faster than the other
# we deal with this by doing while left is still in bounds...set arr[i] to left[j] and increase both pointers
# then do the same check for the right
# this will ensure once of the the lists are done we will add the rest of the leftover subarray


# 912. Sort an Array
# Attempted
# Medium
# Topics
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104