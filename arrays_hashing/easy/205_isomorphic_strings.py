class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      st, ts = {}, {}

      for i in range(len(s)):
        c1, c2, = s[i], t[i]

        if ((c1 in st and st[c1] != c2) or (c2 in ts and ts[c2] != c1)):
          return False
        
        st[c1] = c2
        ts[c2] = c1


      return True
        

# we go through just one string since they are both same in length or if not theyll be false
# first we have to check if each character is in the hashmap and if that hashmap key has been mapped previously to the correct character
# we do this by checkig if current character is in the hashmap AND if current mapping is NOT the opposite string's character
# we also have to check the opposite 
# for example s = foo t= bar
# we check if f is present in it's hashmap and then if F's match ISNT b...if true return false
# in this example we will tun into problems at the second O and R since O is mapped already in the first hashmap and it isnt to A like the first O
# we return false is either statement checks out
# else we will map each hashmap to the opposite character using each other's current character as the key and the oppo character as the val
# return true if we get to the end

# this will run technically o(2n) but o(n)

# 205. Isomorphic Strings
# Easy
# Topics
# Companies
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
 

#  https://pythontutor.com/render.html#code=class%20Solution%3A%0A%20%20%20%20def%20isIsomorphic%28self,%20s%3A%20str,%20t%3A%20str%29%20-%3E%20bool%3A%0A%20%20%20%20%20%20st,%20ts%20%3D%20%7B%7D,%20%7B%7D%0A%0A%20%20%20%20%20%20for%20i%20in%20range%28len%28s%29%29%3A%0A%20%20%20%20%20%20%20%20c1,%20c2,%20%3D%20s%5Bi%5D,%20t%5Bi%5D%0A%0A%20%20%20%20%20%20%20%20if%20%28%28c1%20in%20st%20and%20st%5Bc1%5D%20!%3D%20c2%29%20or%20%28c2%20in%20ts%20and%20ts%5Bc2%5D%20!%3D%20c1%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20st%5Bc1%5D%20%3D%20c2%0A%20%20%20%20%20%20%20%20ts%5Bc2%5D%20%3D%20c1%0A%0A%0A%20%20%20%20%20%20return%20True%0A%0A%0Ab%20%3D%20Solution%28%29%0Ab.isIsomorphic%28%22foo%22,%20%22bar%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false