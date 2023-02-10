class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        res, flag = 0, 0
        visited = []
        for i in s:
            if i not in visited:
                char_count = s.count(i)
                
                if char_count % 2 == 0:
                    res += char_count
                else:
                    char_count = char_count - 1
                    res += char_count
                    flag = 1
            visited.append(i)
        if flag == 1:
            return res + 1
        else:
            return res