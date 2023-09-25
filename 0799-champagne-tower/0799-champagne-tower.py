class Solution:        
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = [poured]
        for i in range(1, query_row+1):
            curr_row = [0] * (i+1)
            for j, v in enumerate(memo):
                if v > 1:
                    half = (v-1)/2
                    curr_row[j] += half
                    curr_row[j+1] += half
            
            memo = curr_row
        return min(1, memo[query_glass])