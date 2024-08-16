# Given an array of strings strs, group the anagrams together. you can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase. typically using all the original letter exactly once.

# Example 1.
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# we want to pick each word in the strs and check if it's combination letter is already a key in the hashmap.
# if it exist lets add it to the array associated with the key. we move to the next string and check if it's 
# combination letter is a key in the hasmap, if yes add it to the array is associated with. 
#  all we have to do is go through the value in the hasmap and appen them to an array

#  Solution:
# we create our anagram as an empty map
# since our result has to be an array, so we create our result as an empty array
# anagram_map = {}
# result = [] ... we will add value to it later

# the first to do is to go through each of the word and check if it's an anagram and for which anagram. 
# we need to add the anagram map. 

# i.e., for s in strs:
 
#  to make easy to get if those words are the same anagram. we will use sort method
# with that it arrange all the values in strs in alphabetical other and arrange them beside each other 
# i.e., 
# for s in strs:
#    sorted_s = sorted(s)
# then we add it to the anagram map 
# i.e.,
# sorted_s is now a key we can use to save into our anagram_map
#    i.e., anagram_map[sorted_s].append(s)

# but since we don't have the key initialized in our anagram we are goin to have error
# so we are going to use a defaultdict. we import defaultdict from collections 
# from collections imports defaultdict 
# so we are going to replace python standard dictionary with defaultdict
# and set the type of the defaultdict into list. so we want each key we want to adding to adding to the anagram_map we want the default value to be an empty list
# we have:
#  anagram_map = defaultdict(list)

# the second error we will get is that we are using a list as the the key because sorted_s is a mutable type which is a list
# and a mutable type can not be used as a key. so we have to convert it to immutable type which is a tuple
# we have:
# sorted_s = tuple(sorted(s))

# now if we check our anagram_mao we have a dictlist that cointains sorted_s as the key and s(the actual words that was sorted and gave thesame result as values)
# i.e

# anagram_map = [[['a','e','t']:["ate","eat","tea"]], [['a','n','t']:["nat",tan]]]

# what we need is the value not the keys.
# so we append the value to the results which is an empty list

# so we iterate over anagram_map values and append them to result..

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagram(self, strs: List[str])-> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        for value in anagram_map.values():
            result.append(value)
        return result
