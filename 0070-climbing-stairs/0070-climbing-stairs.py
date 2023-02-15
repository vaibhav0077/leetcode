class Solution:
    def climbStairs(self, n: int) -> int:
    
        dp = [-1 for i in range(n)]
        def sol(i):
            if i == n: return 1
            if i > n : return 0
            if dp[i] != -1: return dp[i]
            
            two = 0
            if n-i > 1:
                two = sol(i+2)
            one = sol(i+1)
            
            dp[i] = one + two
            return dp[i]
        
        sol(0)
        return dp[0]
            