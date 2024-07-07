# Given an array of integers, retutn indices of the two numbers such that they add up to a specific target. 
# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Example

# Given nums = [2, 7, 11, 15], target = 9,

# Because num[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]

# Tip

# 1. check the sum of combination of every two input and see if they equate to target.
# 2. we check from the first input and check if their sum with any other input is equal to target.
# 3. if the first round with the first input is not equal to target then we move to the next input
# 4. note since we've checked the first element and it did not work, we don't need to check it again.
# 5. so we need to check with the second input and the other input that follows it

# The runtime of the algorightm is not supper efficient, this is brute force, we are are going through the entire legnth of the array (N) and do it for each (N) time
#         N.N
# worst case time of complexity will be 
#             N.N = 0(N²)

# [2, 7, 11, 15], target = 9
# what we are trying to do is to minus the target from each input and see if the result exit in the array
# the best soluton is to use HASHMAP. hasmap all the array input.
# so in our hashmap we will be matching all the input to the Index
#         0  1  2    3
#        [2, 7, 11, 15] 

# The best way to do it is to assume our hashmap is empty, minus the target from the first index and add it to the hashmap and do this for all the input vlue in the array


# HASHMAP                 0       1     2       3
# val:Index               2       7     11      15
# 2  : 0                  9-2    9-7   9-11     9-3
# 7  : 1
# 11 : 2
# 15 : 3

# what we are going to do is is to assume our hashmap has only two value which equate to our target. and make sure no value exist before the fist input, also no value exit till we get to our next value. with this
# our time complexity 
#                             Time = 0(N)
# we are using extra memery so memmory will be equal to 
#                             mem : 0(N)

from typing import List

class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        prevHash = {}
        for i, n in enumerate(num):
            diff = target - n
            if diff in prevHash:
                return [prevHash[diff], i]
            prevHash[n] = i
        return []