class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
      res = 0
      for i in range(len(tickets)):
        if i <= k:
          res += min(tickets[i], tickets[k])
        else:
          res += min(tickets[k] -1, tickets[i])
      return res
    
# o(n) runtime and constant time space
# we iterate through the list of tickets by index
# if the index is before or right at kth position then we must wait for these to zero out to buy all tickets
# if this is the case then we add the minimum between tickets/seconds at that position or kth position
#   this means which position will zero out first between kth and ith where i is before the kth postion
# if i is after the kth index then we do not have to wait for these positions to zero out
# we just need the minimum between ith index and kth index but kth index -1 because we wouldnt need to do a full rotation of the line
# for example 23456 while k is 0.....we will stop after 2 rotations so we wouldnt take the full 2 seconds just 1
# first rotation would be 12345...then 01234 but we stop right after we hit the quota of 2 tickets for postion k=0

# 2073. Time Needed to Buy Tickets
# Easy
# Topics
# Companies
# Hint
# There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

# You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

# Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

# Return the time taken for the person at position k (0-indexed) to finish buying tickets.

 

# Example 1:

# Input: tickets = [2,3,2], k = 2
# Output: 6
# Explanation: 
# - In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
# - In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
# The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
# Example 2:

# Input: tickets = [5,1,1,1], k = 0
# Output: 8
# Explanation:
# - In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
# - In the next 4 passes, only the person in position 0 is buying tickets.
# The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.
 

# Constraints:

# n == tickets.length
# 1 <= n <= 100
# 1 <= tickets[i] <= 100
# 0 <= k < n