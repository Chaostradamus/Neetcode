class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
      s = set()
      for p in paths:
        s.add(p[0])

      for p in paths:
        if p[1] not in s:
          return p[1]
        

# o(n) runtime and space because one hashset and one time through each path
# we add each starting city to a hashset
# we then iterate through each second city checking if it is in the hashset, the one that doesnt go to an outgoing city will not be in the hashset
# we have to do it this way because the first starting city is not always the starting path for the journey. (what?!) 
# misunderstood the question

# 1436. Destination City
# Easy
# Topics
# Companies
# Hint
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

# Example 1:

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
# Example 2:

# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".
# Example 3:

# Input: paths = [["A","Z"]]
# Output: "Z"
 

# Constraints:

# 1 <= paths.length <= 100
# paths[i].length == 2
# 1 <= cityAi.length, cityBi.length <= 10
# cityAi != cityBi
# All strings consist of lowercase and uppercase English letters and the space character.