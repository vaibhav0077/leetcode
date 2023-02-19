class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = [0 for i in range(26)]
        chek = [0 for i in range(26)]
        ans = []
        n = len(s)
        m = len(p)
        j = 0
        
        if n < m: return []
        
        while j < m:
            freq[ord(p[j])-97] +=1
            j+=1

        k = 0
        while k < m:
            chek[ord(s[k])-97] +=1
            k+=1
        
        if chek == freq: ans.append(0)
            
        i = m
        while i < n:
            chek[ord(s[i])-97] +=1
            chek[ord(s[i-m])-97] -=1
            
            if chek == freq:
                ans.append(i-m+1)
            i+=1
        
        return ans
            
            