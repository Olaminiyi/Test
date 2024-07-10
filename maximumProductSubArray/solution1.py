# from typing import List

# class Solution:
#     def maxProductSubArray(self, nums: List[int]) -> int:
#         minProd = nums[0]
#         maxProd = nums[0]
#         prodMax = nums[0]

#         for i in nums[1:]:
#             if i == 0:
#                 minProd = maxProd = 0
#             else:
#                 if i < 0:
#                     minProd, maxProd = maxProd, minProd
                    
#                 maxProd = max(i, maxProd * i)
#                 minProd = min(i, minProd * i)

#             prodMax = max(prodMax, maxProd)
#         return prodMax
