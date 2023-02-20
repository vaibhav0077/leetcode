class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        finals = ""
        finalt = ""
        
        for x in s:
            finals += x
            if x == "#":
                finals = finals[:-2]
        
        for x in t:   
            finalt += x
            if x == "#":
                finalt = finalt[:-2]
        
        return finals == finalt
                
                
            
            
        