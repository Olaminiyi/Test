from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int])-> bool:
        saveset = set()

        for n in nums:
            if n in saveset:
                return True
            saveset.add(n)
        return False