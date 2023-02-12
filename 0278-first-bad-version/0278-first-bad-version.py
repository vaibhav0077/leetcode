# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n
        prevBad = None
        
        while left <= right:
            
            mid = (left + right) // 2
            x = isBadVersion(mid)
            if x:
                prevBad = mid
            
            if x:
                right = mid -1
            else:
                left = mid + 1
        return prevBad
        
        
                
            
            
            