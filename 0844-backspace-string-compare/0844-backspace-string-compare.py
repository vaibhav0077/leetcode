class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        fs = ""
        ft = ""
        for x in s:
            if x == "#":
                fs = fs[:-1]
            
            else:
                fs += x
        
        for x in t:
            if x == "#":
                ft = ft[:-1]
            
            else:
                ft += x
        
        return fs == ft