class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dupele = 0
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                dupele+=1
                if dupele > 1:
                    nums.pop(i)
                    i-=1
            else:
                dupele = 0
            i+=1