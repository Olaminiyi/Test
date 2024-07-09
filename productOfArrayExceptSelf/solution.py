# Given an integer array nums, return an array answer such that answer[i] is equal to the product
# of all the elements of nums except num[i].

# The product of any prefix or suffix of num is guranteed to fit in a 32-bit integer

# You must write an algorithm that run in o(n) without using the division operation

# Example 1:
# Input: nums = [1,2,3,4]
# output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res