class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            diff = totalSum - nums[i] - leftSum
            
            if diff == leftSum:
                return i
            else:
                # totalSum-= nums[i]
                leftSum+= nums[i]
        return -1
            
            
        