class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}
        
        def sol(i, remain):
            if remain <= 0:
                return 0
            if i == len(cost): return float('inf')
            if (i, remain) in dp: return dp[(i, remain)]
            
            
            paint = cost[i] + sol(i+1, remain - time[i] -1)
            skip = sol(i+1, remain)
            
            dp[(i, remain)] = min(paint, skip)
            return dp[(i, remain)]
        
        sol(0, len(cost))
        return dp[(0, len(cost))]