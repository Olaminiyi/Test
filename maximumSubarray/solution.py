# Given an integer array nums. find the contiguous subarray (containing
# at least one number) which has the largest sum and return its sum

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4]
# output: 6 
# Explanation: [4,-1,2,1] has the largest sum = 6 

# We are to find a sub array within an array that will give highest number when added together.
# our trick is to use pointers or cursor and start from the leftmost. 

# we keep incrementing our right pointer as we go through the array but our left poniter 
# keeps getting getting shifted if we get  ever get a -ve prefix,
# so anytime we get a a negative prefix we remove it 
# Just like a sliding window. time complexity o(n) 

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = float('-inf') #to initialize a variable to the lowest possible value, any real number in the list will be larger
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            maxSub = max(maxSub, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
           
        return maxSub