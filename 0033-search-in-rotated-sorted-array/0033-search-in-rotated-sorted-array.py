class Solution:
    def search(self, nums: List[int], target: int) -> int:
        value = -1
        for i in range(len(nums)):
            if nums[i] == target:
                value = i
                break
        return value