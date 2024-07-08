# # given an array nums, return true if any value appperas at least twice in the array,
# # and return false if every element is distinct

# # Example 1: 
# # input: nums = [1, 2, 3, 1]
# # output: true 

# # Example 2: 
# # Input: nums = [1, 2, 3, 4]
# # output: false 

# Similar to hash table, a hash set is also a collection of objects. 
# In hash table, data was stored in the form of key-value pairs, 
# whereas in hash sets, the data is stored as objects. 
# A hash set internally uses the hash table data structure to store data items. 
# Just like a set, a hash set also does not allow storage of duplicate elements.


# We use " del, pop, and popitem()" to delete an item in hash table

# we use "pop,remove, discard" to remove item in the hashset
# clear(): it completely empties the set 
# del(): this delete the set 

# **Hash map is also know as dictionary**
# Use a hash set when you need to efficiently check for the presence of elements in a collection 
# and ensure uniqueness (no duplicates).
# A common use case is when you want to find unique elements or 
# identify whether there is any overlap between two collections.

# Hash table store key-value pairs and the key is generated through a function called hash function

from typing import List 

class Solution:
    def containsDuplicate(self, nums: List[int])-> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False