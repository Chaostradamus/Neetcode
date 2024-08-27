class ListNode:
  def __init__(self, key):
    self.key = key
    self.next = None

    # listnode class that just has a key and next = none

class MyHashSet:


    def __init__(self):
      self.set = [ListNode(0) for i in range(10**4)]

    #   constructor creating an array of listnodes with key of 0 initially
        

    def add(self, key: int) -> None:
      cur = self.set[key % len(self.set)]
      while cur.next:
        if cur.next.key == key:
          return
        cur = cur.next
      cur.next = ListNode(key)
    #   we set cur to the set at the given key modulo by length of set. this is our hashing function
    # this gives us the current index(hashed key)
    # we traverse the given index at that index skipping the listnode(0) which is the dummy node
    # if we find a duplicate then we return because we cannot add the given key(value)
    # else we will get to the end and append a new listnode with the given value
        

    def remove(self, key: int) -> None:
      cur = self.set[key % len(self.set)]
      while cur.next:
        if cur.next.key == key:
          cur.next = cur.next.next
          return
        cur = cur.next
    #   works the same as add except we find the key in at the listnode linked list and break the linked list pointer by setting
    # it as next.next

        

    def contains(self, key: int) -> bool:
      cur = self.set[key % len(self.set)]
      while cur.next:
        if cur.next.key == key:
          return True
        cur = cur.next
      return False
        # will work the same as the other ones except we just find the key value and return true else return false
      
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



# 705. Design HashSet
# Solved
# Easy
# Topics
# Companies
# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
 

# Constraints:

# 0 <= key <= 106
# At most 104 calls will be made to add, remove, and contains.