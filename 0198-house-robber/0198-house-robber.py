class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = prev_prev = 0
        for i in range(0, len(nums)):
            nottake = 0
            if i-1>=0:
                nottake += prev
            take = nums[i]
            if i-2 >= 0:    
                take  += prev_prev
                
            prev_prev = prev
            prev = max(nottake, take)
            
        return prev