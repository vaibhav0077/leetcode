class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = list(set(nums))
        nums.sort()

        start = 0
        ans = float('inf')

        while(start<len(nums)):
            target = nums[start] + n - 1
            ip = bisect_left(nums, target, lo= 1, hi= len(nums)-1)

            if ip == len(nums) or nums[ip]>target:
                ip -= 1

            ans = min(ans, (n-1)-(ip-start))

            start += 1
        return ans