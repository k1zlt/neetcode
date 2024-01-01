from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            k = len(s)
            s.add(i)
            if k == len(s):
                return True      
        return False