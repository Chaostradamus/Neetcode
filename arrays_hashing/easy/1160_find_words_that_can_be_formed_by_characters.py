class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
      count = {}
      for c in chars:
        if c in count:
          count[c] += 1
        else:
          count[c] = 1
      res = 0

      for w in words:
        cur_word = defaultdict(int)
        good = True
        

        for c in w:
          cur_word[c] += 1
          if cur_word[c] > count.get(c, 0):
            good = False
            break
        if good:
          res += len(w)
      return res


# time is (n * k + m) where n is avg size of each word and k is #of words + m which is size of chars
# space is (n+m) where n and m are size of both hashmaps
# first we populate character hashmap with the count of each
# then we iterate through each word one by one and each character of each word
# we will also keep a boolean flag of each word set initially to true
# we will also fill out a hashmap for each word's character count but check that hashmap against the main characters hashmap each time 
# we count a letter
# if the count of the words' letter is greater than the count in the character hashmap at anytime we change good to false and break
# at the end of the check on a single word, if the word is still considered boolean flagged good then we add to a res variable
# that keeps track of the total len so far


# 1160. Find Words That Can Be Formed by Characters
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

 

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.