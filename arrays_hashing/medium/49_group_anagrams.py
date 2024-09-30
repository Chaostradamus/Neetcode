class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = defaultdict(list)

      for s in strs:
        count = [0] * 26

        for c in s:
          count[ord(c) - ord('a')] += 1

        res[tuple(count)].append(s)
        
      return res.values()
        
# create a defaultdict for as a hashmap
# we iterate through every word in strings
#    we create a coune with 26 0's signifying the alphabet from 0 to 25
#   for every string we iterate through every letter and fill in the count array
#   we the populate res with each word using the key as the count of the words letters
#   and the value as the word
#   on each word it will populate the count and if it matches any previous key it will group the anagrams together
# return res.values

# this is o(m *n) where n is length of strings and m is number of strings given

# why use default dict
# Using a defaultdict from the collections module in Python provides a convenient way to handle missing keys in a dictionary. When you access a key that doesn't exist in a defaultdict, it automatically creates an entry for that key using a default factory function that you provide. This helps to avoid KeyError exceptions and makes the code cleaner and more readable.

# Here's why you might use a defaultdict with a list as the default factory:

# Automatic Initialization: If you access a key that doesn't exist, defaultdict will automatically create a new list for that key. This eliminates the need to check if the key exists and initialize it manually.

# Simplifies Code: It reduces boilerplate code. You don't need to write code to handle missing keys, making your code shorter and more concise.

# Improves Readability: The intent of the code is clearer, as you specify up front that the default value for each key is a list.


# why use a tuple
# In the groupAnagrams method, a tuple is used as the key for the defaultdict. This approach leverages the immutability and hashability of tuples to effectively group anagrams. Here's a deeper explanation:

# Why Use a Tuple?
# Immutability: Tuples are immutable, meaning their contents cannot be changed after creation. This property is essential because dictionary keys must be immutable to ensure the integrity of the key-value mapping.

# Hashability: Tuples are hashable, which means they can be used as keys in dictionaries. Lists, on the other hand, are not hashable because their contents can change, which would affect their hash value.




# 49. Group Anagrams
# Solved
# Medium
# Topics
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# https://pythontutor.com/render.html#code=from%20typing%20import%20List%0Afrom%20collections%20import%20defaultdict%0A%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20groupAnagrams%28self,%20strs%3A%20List%5Bstr%5D%29%20-%3E%20List%5BList%5Bstr%5D%5D%3A%0A%20%20%20%20%20%20res%20%3D%20defaultdict%28list%29%0A%0A%20%20%20%20%20%20for%20s%20in%20strs%3A%0A%20%20%20%20%20%20%20%20count%20%3D%20%5B0%5D%20*%2026%0A%0A%20%20%20%20%20%20%20%20for%20c%20in%20s%3A%0A%20%20%20%20%20%20%20%20%20%20count%5Bord%28c%29%20-%20ord%28'a'%29%5D%20%2B%3D%201%0A%0A%20%20%20%20%20%20%20%20res%5Btuple%28count%29%5D.append%28s%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20return%20res.values%28%29%0A%20%20%20%20%20%20%0A%0Ab%20%3D%20Solution%28%29%0Ab.groupAnagrams%28%5B%22eat%22,%22tea%22,%22tan%22,%22ate%22,%22nat%22,%22bat%22%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false