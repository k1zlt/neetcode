from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = sorted(nums)
        
        start = 0
        end = len(nums) - 1
        
        while end > start:
            if nums2[end] + nums2[start] > target:
                end -= 1
            elif nums2[end] + nums2[start] < target:
                start += 1
            else:
                return [nums.index(nums2[start]), nums.index[nums2[end]]]
        return None
    
# c = Solution()

# print(c.twoSum([1, 2, 3, 4, 5, 6], 3))