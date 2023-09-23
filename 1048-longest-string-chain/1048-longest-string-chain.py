class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        words = sorted(words, key=len)
        dp = [1] * len(words)
        
        def comparei(s1, s2):
            if len(s1) != len(s2)+1:
                return 0
            
            first = 0
            second = 0
            
            while first < len(s1):
                if second < len(s2) and s1[first] == s2[second]:
                    second+=1
                first+=1
            
            if second == len(s2) :
                return 1
            return 0
                
            
        
        for i in range(0, len(words)):
            for j in range(0, i):
                
                if comparei(words[i], words[j]) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j]+1
        
        return max(dp)