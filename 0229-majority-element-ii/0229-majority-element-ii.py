class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n = n//3
        temp = []
        t = {}
        for x in nums:
            if x in t:
                t[x] += 1
            else:
                t[x] = 1
        
        for keys in t:
            if t[keys] > n:
                temp.append(keys)
        
        return temp
        