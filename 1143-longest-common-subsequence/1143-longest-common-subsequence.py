class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        matrix = [[-1 for i in range(m)] for j in range(n)]
        
        def dp(i, j):
            
            if i < 0 or j < 0:
                return 0
            if matrix[i][j] != -1 :return matrix[i][j]
            
            if text1[i] == text2[j]:
                matrix[i][j] =  1 + dp(i-1,  j-1)
            else:
                matrix[i][j] = max(dp(i-1, j), dp(i, j-1))
            
            return matrix[i][j]
    
        return dp(n-1, m-1)