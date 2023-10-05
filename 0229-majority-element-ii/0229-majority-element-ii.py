class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = list(set(nums))
        l = len(nums)//3
        res = []

        for i in n:
            if nums.count(i) > l:
                res.append(i)
        
        return res