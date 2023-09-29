class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: continue
            if nums[i] > nums[i+1]:
                decreasing=True
            else:
                increasing=True
            break
        for i in range(len(nums)-1):
            if (increasing and nums[i]<=nums[i+1]) or (decreasing and nums[i] >= nums[i+1]):
                continue
            elif (not increasing and not decreasing):
                return True
            else:
                return False
        return True
                
            
                