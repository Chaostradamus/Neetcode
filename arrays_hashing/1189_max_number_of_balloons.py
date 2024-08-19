class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
      countText = Counter(text)
      balloon = Counter("balloon")
      res = len(text)

      for c in balloon:
        res = min(res, countText[c] // balloon[c])
      return res
        


# o(n) runtime and space
# populate 2 hashmaps with the input text and the word balloon
# set result to length of the text because it is a safe number to set it as
# iterate through each "letter" in balloon hashmap
# take the min of res or the number you get from the ratio of the hashmaps from text and balloon
# for example if text has 3 L's then you divide 3 by 2 you get 1 ...remainder is thrown out
# if theres 5 L's then you do 5//2 and get 2 and remainder is thrown out
# integer division means to just take the answer without remainder
# we take the smallest ratio from the text hashmap // balloon hashmap as our answer because the smallest number is the roadblock 
# return res


# 1189. Maximum Number of Balloons
# Easy
# Topics
# Companies
# Hint
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0