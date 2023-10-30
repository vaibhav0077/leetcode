class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def DecimalToBinary(n): 
            return bin(n).replace("0b", "") 

        a = {}
        ans = []

        for x in arr:
            counti = DecimalToBinary(x).count("1")
            if counti in a:
                a[counti].append(x)
            else:
                a[counti] = [x]

        for key in sorted(a.keys()):
            arri = a[key]
            arri.sort()
            ans += arri

        return ans