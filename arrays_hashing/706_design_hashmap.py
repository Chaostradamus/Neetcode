class ListNode:
  def __init__(self, key=-1, val=-1, next=None):
    self.key = key
    self.val = val
    self.next = next


    # listnode classinitially set with -1 key -1 val and no next


class MyHashMap:

    def __init__(self):
      self.map = [ListNode() for i in range(1000)]

    #   populate an array with 1000 buckets that each contain a dummy node initially
        
    def hash(self, key):
      return key % (len(self.map))
    
    # hashing function that takes a key and returns the key modulo by the length of the map which is told to be 1000


    def put(self, key: int, value: int) -> None:
      cur = self.map[self.hash(key)]
      while cur.next:
        if cur.next.key == key:
          cur.next.val = value
          return

        cur = cur.next
      cur.next = ListNode(key, value)

    #   we set cur to the maps's buckey at position of the hashed key
    # while theres a cur.next (since we are at the dummy node initially)
    # if the cur.next key matches then we reset that node's val to value and return
    # else we wil continue traversing
    # if we get to the end then we didnt find the key in this bucket yet so we create a new listnode with key/val as the cur.next
        

    def get(self, key: int) -> int:
      cur = self.map[self.hash(key)].next
      while cur:
        if cur.key == key:
          return cur.val
        cur = cur.next
      return -1       
    # we set cur to the map at index of hashed key. we move off the dummy node with .next since we are retrieving
    # while cur exists we will traverse it look for matching keys and then returning values
    # else we will return -1

    def remove(self, key: int) -> None:
      cur = self.map[self.hash(key)]
      while cur and cur.next:
        if cur.next.key == key:
          cur.next = cur.next.next
          return
        cur = cur.next

        # for the remove function we will again start cur of map at hashed key's bucket and traverse the linked list
        # while there are both cur and cur.next to stay in bounds
        # if we find matching keys we will pointer manipulate by moving cur.next to cur.next.next and return
        



      
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# 706. Design HashMap
# Solved
# Easy
# Topics
# Companies
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

# Constraints:

# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.