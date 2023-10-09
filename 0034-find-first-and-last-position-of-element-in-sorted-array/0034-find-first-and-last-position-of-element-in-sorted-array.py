class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ft, lt = 10**10, -1
        for i in range(len(nums)):
            if nums[i] == target:
                ft = min(i, ft)
                lt = max(i, lt)
        
        if ft == 10**10: ft = -1
        
        return [ft, lt]