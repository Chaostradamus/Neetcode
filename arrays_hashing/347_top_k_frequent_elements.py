class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) +1)]

        for n in nums:
          count[n] =1 + count.get(n, 0)
        for n, c, in count.items():
          freq[c].append(n)


        res = []
        for i in range(len(freq) -1, 0, -1):
          for n in freq[i]:
            res.append(n)
            if len(res) == k:
              return res
            
# neetcode solution with bucket sort
# we fill an array with the index as the frequency and the element as the element of the index
#for example if 6 occurs 24 times, we store 6 at 24th index
# we create an array the size of the len(nums) +1
# create a hashmap and ifll in for element and count and then store frequency and element in the array
# we iterate backwards from the array and reutnr once len of res array is equal to k

# Time Complexity
# Counting Frequencies:

# The first loop counts the frequency of each number in nums, which takes O(n) time, where n is the number of elements in nums.
# Organizing by Frequency:

# The second loop iterates through the count dictionary. Since the maximum frequency of any number can be at most n, this loop also runs in O(n) time in the worst case.
# Building the Result:

# The third part iterates through the freq list in reverse order, which can take up to O(n) in the worst case. The inner loop goes through the elements in freq[i], and you stop when you have collected k elements.
# Overall Time Complexity
# Combining all parts:

# Total Time Complexity
# =
# 𝑂
# (
# 𝑛
# +
# 𝑛
# +
# 𝑛
# )
# =
# 𝑂
# (
# 𝑛
# )
# Total Time Complexity=O(n+n+n)=O(n)
# So, the overall time complexity is O(n).

# Space Complexity
# Count Dictionary:

# The count dictionary holds the unique elements from nums, so its space complexity is O(m), where m is the number of unique elements. In the worst case, this could be O(n) if all elements are unique.
# Frequency List:

# The freq list contains lists for each possible frequency from 0 to n, so it uses O(n) space in the worst case.
# Result List:

# The res list can hold up to k elements, so it requires O(k) space.
# Overall Space Complexity
# Combining all parts:

# Total Space Complexity
# =
# 𝑂
# (
# 𝑚
# +
# 𝑛
# +
# 𝑘
# )
# =
# 𝑂
# (
# 𝑛
# )
# (in the worst case)
# Total Space Complexity=O(m+n+k)=O(n)(in the worst case)
# Thus, the overall space complexity is also O(n) in the worst case.

# Comparison
# The algorithm you provided is O(n) in both time and space complexity, which is more efficient than the previous algorithms that had O(n log n) time complexity due to sorting.
# Summary
# Time Complexity: O(n)
# Space Complexity: O(n)



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
          if num in freq:
            freq[num] += 1
          else:
            freq[num] = 1

        fmap = list(freq.items())
        fmap.sort(key=lambda x: x[1], reverse = True)
        res = [item for item,count in fmap]

        return res[:k]
# chat gpt solution
#we fill  up the hashmap with the nums and their count
# we convert the hashmap into a list of tuples
# we sort the list of tuples with a lambda function which sorts by x where x[1]
# which means we sort by the second element in each tupe ppair
# we set reverse to true to sort in descending order
# we create another array which just takes in the elements and return the array from :k 

# Time Complexity
# Counting Frequency:

# The loop for num in nums: iterates over all n elements in the nums list.
# Inside the loop, checking if num is in freq_map and updating the count takes constant time, O(1), on average.
# Therefore, the time complexity for counting frequencies is O(n).
# Creating the Frequency List:

# freq_list = list(freq_map.items()) creates a list of tuples from the dictionary.
# This operation takes O(m) time, where m is the number of unique elements in freq_map. In the worst case, m can be up to n, so this step is O(n).
# Sorting:

# The sorting step freq_list.sort(key=lambda x: x[1], reverse=True) sorts the list of tuples based on the frequency.
# Sorting has a time complexity of O(m log m). In the worst case, if all elements are unique, this becomes O(n log n).
# Extracting the Top K Elements:

# The list comprehension top_k = [item for item, count in freq_list[:k]] takes O(k) time.
# Since k is typically much smaller than n, this step can be considered O(k).
# Total Time Complexity
# Combining all the steps, the overall time complexity is:

# Time Complexity
# =
# 𝑂
# (
# 𝑛
# +
# 𝑛
# +
# 𝑛
# log
# ⁡
# 𝑛
# +
# 𝑘
# )
# =
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# Time Complexity=O(n+n+nlogn+k)=O(nlogn)
# The dominant term is O(n log n) due to the sorting step.

# Space Complexity
# Frequency Map:

# The dictionary freq_map stores counts for each unique element in nums, which requires O(m) space, where m is the number of unique elements. In the worst case, this can be O(n).
# Frequency List:

# freq_list is a list of tuples created from freq_map, requiring O(m) space. Again, in the worst case, this can also be O(n).
# Top K List:

# The list top_k holds the top k elements, which requires O(k) space.
# Total Space Complexity
# Combining all the components, the overall space complexity is:

# Space Complexity
# =
# 𝑂
# (
# 𝑚
# +
# 𝑚
# +
# 𝑘
# )
# =
# 𝑂
# (
# 𝑛
# +
# 𝑘
# )
# Space Complexity=O(m+m+k)=O(n+k)
# Thus, the total space complexity is O(n) in the worst case, assuming k is smaller compared to n.

# Summary
# Time Complexity: O(n log n)
# Space Complexity: O(n + k)


from collections import Counter

nums = [1, 1, 1, 2, 2, 3]
freq_map = Counter(nums)

# freq_map.most_common(2) returns [(1, 3), (2, 2)]

# Correct way to unpack the tuples
top_k = [item for item, count in freq_map.most_common(2)]
print(top_k)  # Output: [1, 2]

# Time Complexity:
# Counting the frequency: O(n), where n is the length of nums.
# Sorting by frequency using most_common(k): This internally sorts the elements by frequency, which takes O(n log n).
# So the overall time complexity is O(n log n).
# This solution is simple and works efficiently when k is not significantly smaller than n.

# Total Space Complexity
# Combining both parts:

# The space used by freq_map is O(n).
# The space used by top_k is O(k).
# Therefore, the overall space complexity of the function is:

# Space Complexity
# =
# 𝑂
# (
# 𝑛
# +
# 𝑘
# )
# Space Complexity=O(n+k)
# This means that the space complexity is primarily dependent on the number of unique elements in nums and the number of top elements you want to return.

# chatgpt more efficient but uses built in functions
# we put nums into a counter function hashmap
# we iterate over the pairs and just take the key and use the most common function and pass in k
# this return just the most common up to k in an array for us





# 347. Top K Frequent Elements
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
