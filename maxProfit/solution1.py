from typing import List
class Solution:
    def maxProfit(self,sum: List[int])-> int:
        l, r = 0,1
        maxP = 0
        while r < len(sum):
            if sum[r] > sum[l]:
                ans = sum[r] - sum[l]
                maxP = max (ans, maxP)
            else:
                l = r
            r += 1
        return maxP
