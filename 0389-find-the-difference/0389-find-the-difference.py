class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for x in s:
            t = t.replace(x, '', 1)
        
        return t