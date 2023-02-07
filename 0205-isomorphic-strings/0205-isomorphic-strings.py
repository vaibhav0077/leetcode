class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        
        def get_key(val):
            for key, value in dic.items():
                if val == value:
                    return key
        
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in dic.keys():
                if dic[s[i]] != t[i]:
                    return False
            else:
                if not t[i] in dic.values():
                    dic[s[i]] = t[i]
                else:
                    temp = get_key(t[i])
                    if temp != s[i]:
                        return False
                    
        
        return True
                
        