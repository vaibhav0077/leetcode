class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        l_vowel = sum(map(s[:n].count, ['a','e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U']))
        r_vowel = sum(map(s[n:].count, ['a','e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U']))
        # print(l_vowel, r_vowel,n)
        if l_vowel==r_vowel: return True
        return False
        
        