class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        ans = -10**7
        dp = [[-10**7 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j],  dp[i][j] + nums1[i]*nums2[j], nums1[i]*nums2[j])
            ans = max(dp[i] + [ans])
        
        ans = max(dp[n] + [ans])
        return ans