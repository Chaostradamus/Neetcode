class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
      unique = set()
     
      

      for e in emails:
        i = 0    
        local = ""
        domain = ""    
        while e[i] not in ["+", "@"]:
          if e[i] != ".":
            local += e[i]
          i += 1
        while e[i] != "@":
          i += 1
        domain = e[i+1 :]
        unique.add((local, domain))
      return len(unique)

# o(n) time and space
# create a set to eliminate duplicates
# iterate through emails
# IMPORTANT TO DECLARE LOCAL AND DOMAIN HERE AND NOT AT THE BEGINNING OF THE CODE...MUST BE DONE IN THIS SCOPE
# TO REEMPTY THEM EACH EMAIL ITERATION
# we will keep a pointer and go through each email
# while the current character isnt a + or @ symbol
# and if its not a "." we will add to local variable
# after that is done we will have successfully parsed the first part of the email before the @
# we will while loop again to the @ symbol of the email
# we do this by while looping each character isnt the @ symbol
# once we find it we will set the domain variable as the i + 1 (for indexing) to the end of that string
# then we add it to the hashSet which will not add duplicates
# return the length of the hashSet

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
      unique = set()
     
      

      for e in emails:
        local , domain = e.split("@")
        local = local.split("+")[0]
        local = local.replace(".","")
        unique.add((local,domain))
       
      return len(unique)
    
# this solution uses built in functions to split the string at the @ symbol
# then we split the first part of that by the + signs but only taking the first cart off part
# then we replace all "." with blank spaces
# we add local and domain to the hashset 
# we return the length of the hashset at the end

# 929. Unique Email Addresses
# Easy
# Topics
# Companies
# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

# Example 1:

# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
# Example 2:

# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3
 

# Constraints:

# 1 <= emails.length <= 100
# 1 <= emails[i].length <= 100
# emails[i] consist of lowercase English letters, '+', '.' and '@'.
# Each emails[i] contains exactly one '@' character.
# All local and domain names are non-empty.
# Local names do not start with a '+' character.
# Domain names end with the ".com" suffix.