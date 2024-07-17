from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            result = target - n
            if result in prevMap:
                return [prevMap[result], i]
            prevMap[n] = i
        return []