class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
      self.spots = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
      if self.spots[carType -1] > 0:
        self.spots[carType -1] -= 1
        return True
      return False
    
# constructor will initialize an array mapping big medium and small spots available
# addCar function will just take the car Type (size)
# we will check if theres spots by doing cartype -1 for indexing > 0...that means theres spots
# if theres spots we reduce the number of spots by 1 and return true
# else we will return false

# neetcode #2

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
      self.spots = {
        1: [0, big],
        2: [0, medium],
        3: [0, small]
      }
        

    def addCar(self, carType: int) -> bool:
      newTotal = self.spots[carType][0] + 1
      if newTotal <= self.spots[carType][1]:
        self.spots[carType][0] +=1
        return True


# constructor will initialize a hashmap with car type mapped to a min max array
# addcar keeps a newtotal calling the hashmap by carType and first value(min) and adding 1
# if this new value is <= to max value which we get by calling [array][1]
# we can then update the min total by incrementing by 1 and returning true
# else we will return false


# 1603. Design Parking System
# Easy
# Topics
# Companies
# Hint
# Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

# Implement the ParkingSystem class:

# ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
# bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
 

# Example 1:

# Input
# ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]
# Output
# [null, true, true, false, false]

# Explanation
# ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
# parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
# parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
# parkingSystem.addCar(3); // return false because there is no available slot for a small car
# parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
 

# Constraints:

# 0 <= big, medium, small <= 1000
# carType is 1, 2, or 3
# At most 1000 calls will be made to addCar