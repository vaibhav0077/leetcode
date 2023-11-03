class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        count = 0
        n_t = len(target)
        j = 0
        ans = []
        for i in range(1, n+1):
            if j == n_t: 
                return ans

            if i == target[j]:
                ans.append("Push")
                j+=1
            
            else:
                ans.append("Push")
                ans.append("Pop")            
        
        return ans