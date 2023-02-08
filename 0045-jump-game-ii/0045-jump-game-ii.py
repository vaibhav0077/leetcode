class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        jump = 0
        current = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])

            if i == current:
                current = farthest
                jump+=1

        return(jump)