class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]
        def sol(idx, lenList, lar):
            if idx == n:
                if lenList == k:
                    return 1
                return 0
            # print(idx, lenList, lar)
            if dp[idx][lenList][lar] != -1: return dp[idx][lenList][lar]
            ans = 0
            for i in range(1, m+1):
                if i > lar:
                    ans += sol(idx+1, lenList+1, i)
                else:
                    ans += sol(idx+1, lenList, lar)
                    
                ans = ans%(10**9 + 7)
                
            dp[idx][lenList][lar] = ans
                
            return dp[idx][lenList][lar]
            
        return sol(0,0,0)
        