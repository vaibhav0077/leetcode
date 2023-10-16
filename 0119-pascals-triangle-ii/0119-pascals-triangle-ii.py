class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = {}
        dp[(0,0)] = 1
        dp[(1,0)] = 1
        dp[(1,1)] = 1
        
        for i in range(1, rowIndex+1):
            for j in range(0, i+1):
                left = 0
                upper = 0
                if (i-1,j-1) in dp:
                    left = dp[(i-1,j-1)]
                if (i-1, j) in dp:
                    upper =  dp[(i-1, j)]

                dp[(i, j)]  = left + upper
        ans = []
        for k in range(rowIndex+1):
            ans.append(dp[(rowIndex, k)])
        
        return ans
        