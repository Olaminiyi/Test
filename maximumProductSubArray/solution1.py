from typing import List

class Solutrion:
    def maxProductSubArray(self, nums: List[int]) -> int:
        minProd = nums[0]
        maxProd = nums[0]

        for i in nums[1:]:
            if i < 0:
                maxProd = minProd
                minProd = maxProd
            maxProd = max(i, maxProd * i)
            minProd = max(i, minProd * i)
            prodMax = max(maxProd, minProd)
        return prodMax
