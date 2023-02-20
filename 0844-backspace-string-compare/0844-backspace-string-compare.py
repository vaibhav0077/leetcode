class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        finals = ""
        finalt = ""
        n = len(s)
        m = len(t)
        
        for i in range(n):
            finals += s[i]
            if s[i] == "#":
                finals = finals[:-2]
        
        for i in range(m):    
            finalt += t[i]
            if t[i] == "#":
                finalt = finalt[:-2]
        
        return finals == finalt
                
                
            
            
        