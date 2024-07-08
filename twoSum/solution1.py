from typing import List
class Solution:
    def twoSum(self, num: List[int], target: int)-> List [int]:
        hasMap ={}

        for i, n in enumerate(num):
            ans = target - n
            if ans in hasMap:
                return [hasMap[ans], i]
            else:
                hasMap[n] = i
        return []

# Given nums = [2, 7, 11, 15], target = 9,

# Because num[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]