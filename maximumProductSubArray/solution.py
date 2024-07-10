# Given an integer array nums, find the contiguos subarray within an array 
# (containing at least one number) which has the largest product.

# Example

# Input: [2, 3, -2, 4]
# output: 6
# Explanation: [2,3] has the largest product


from typing import List 

# class Solution:
#     def maxProductSubArray(self, nums: List[int]) -> int:
#         min_p = max_p = nums[0]
#         maximum_product = max_p
#         for num in nums[1:]:
#             temp = min_p
#             min_p = min(num, num*min_p, num*max_p)
#             max_p = max(num, num*temp, num*max_p)
#             maximum_product = max(max_p, maximum_product)
#         return maximum_product


# class Solution:
    # def maxProductSubArray(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0

    #     min_p = max_p = maximum_product = nums[0]

    #     for num in nums[1:]:
    #         if num == 0:
    #             min_p = max_p = 0
    #         else:
    #             if num < 0:
    #                 min_p, max_p = max_p, min_p

    #             max_p = max(num, num * max_p)
    #             min_p = min(num, num * min_p)

    #         maximum_product = max(maximum_product, max_p)
        
    #     return maximum_product

class Solution:
    def maxProductSubArray(self, nums: List[int]) -> int:
        B = nums[::-1] # reversed the nums array

        for x in range(1,len(nums)):
            if nums[x - 1] != 0:
                nums[x] *= nums[x - 1]

            if B[x-1] != 0:
                 B[x] *= B[x-1]
        return max(nums + B)
    
    
# class Solution:
#     def maxProductSubArray(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         max_product = nums[0]
#         current_max = nums[0]
#         current_min = nums[0]

#         for num in nums[1:]:
#             if num < 0:
#                 current_max, current_min = current_min, current_max
            
#             current_max = max(num, current_max * num)
#             current_min = min(num, current_min * num)

#             max_product = max(max_product, current_max)
        
#         return max_product