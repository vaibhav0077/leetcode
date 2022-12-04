class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        rsum = sum(nums)
        lsum = 0
        ans = 0
        temp = float('inf')
        for i in range(n):
            lsum += nums[i]
            rsum -= nums[i]
            b = int(lsum / (i+1))
            a = 0
            if n-i-1>0:
                a = int(rsum / (n-i-1))
            if abs(a-b) < temp:
                ans = i
                temp = abs(a-b)
        return ans

                
        