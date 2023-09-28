class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odda = []
        evena = []
        for x in nums:
            if x%2 == 0:
                evena.append(x)
            else:
                odda.append(x)
        
        return evena + odda
            