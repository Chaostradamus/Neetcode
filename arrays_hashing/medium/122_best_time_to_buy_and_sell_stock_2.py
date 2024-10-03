class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
          if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
        return profit

# o(n) runtime and constant space
# we are just looking for the best times to buy and sell so we only need to look for the days where the previous days are lower than current
# say current day price is 7 and previous is 1 then we are "buying and selling" so  we just tack on profit which is 6. we do
# not need to really buy and sell like what you would typically think when you hear these kinda questions
# we do not need to keep track of more than 2 days to find the answer for max profit with the constraints given in this problemgit add .


# 122. Best Time to Buy and Sell Stock II
# Medium
# Topics
# Companies
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

# Constraints:

# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104