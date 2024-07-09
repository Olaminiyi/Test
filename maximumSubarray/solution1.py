from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = float('-inf')
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i]
            maxSub = max(maxSub, curSum)

            if curSum < 0:
                curSum = 0

        return maxSub