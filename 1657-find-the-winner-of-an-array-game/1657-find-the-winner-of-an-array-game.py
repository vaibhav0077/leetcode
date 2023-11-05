class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
       
        n = len(arr)

        if n*2 < k:
            return max(arr)
        if n == 1: return arr[0]
        
        curr = 0
        win = 1
        if arr[0] < arr[1]:
            curr = 1
        i = 2
        while True:
            if win == k:
                    return arr[curr]

            if arr[curr] > arr[i] or curr == i:
                win+=1
            else:
                curr = i
                win = 1
                
            if i < (n-1):
                i+=1
            else:
                i = 0



