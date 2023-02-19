class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]
        def sol(i, j):
            
            if i>=m or j>=n: return 0
            
            if i == m-1 and j == n-1 : return 1
            
            if dp[i][j] != -1: return dp[i][j]
            
            right = sol(i+1, j)
            down = sol(i, j+1)
            dp[i][j] = right + down
            return dp[i][j]
        
        return sol(0, 0)
        