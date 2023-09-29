from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                for j in range(i, len(nums)):
                    if nums[j] > nums[j - 1]:
                        return False
                return True
            elif nums[i] > nums[i - 1]:
                for j in range(i, len(nums)):
                    if nums[j] < nums[j - 1]:
                        return False
                return True
        return True
