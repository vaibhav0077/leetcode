class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = {}
        
        def sol(curr_index, steps_remain):
            if steps_remain == 0 and curr_index == 0:
                return 1
            
            if curr_index < 0 or curr_index >= arrLen or ( curr_index != 0 and steps_remain == 0): 
                return 0
            
            if (curr_index, steps_remain) in dp:
                return dp[(curr_index, steps_remain) ]
            
            
            left = sol(curr_index - 1, steps_remain -1)
            stay = sol(curr_index , steps_remain -1)
            right = sol(curr_index + 1, steps_remain - 1)
            
            dp[(curr_index, steps_remain)] = (left + stay + right) % (10**9+7)
            
            return dp[(curr_index, steps_remain) ]
        
        sol(0, steps)
        return dp[(0, steps)]