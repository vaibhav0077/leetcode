class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            
            temp1 = stones.pop()
            temp2 = stones.pop()
            stones.append(temp1 - temp2)
        
        return stones[0]