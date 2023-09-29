from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = False

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                increasing = True
            elif nums[i] > nums[i + 1]:
                decreasing = True
            
            # If both increasing and decreasing flags are set, it's not monotonic.
            if increasing and decreasing:
                return False
        
        return True
