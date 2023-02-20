class Solution:
    def decodeString(self, s: str) -> str:
        curstr = ""
        curnum = 0
        sta = []
        
        for x in s:
            
            if x == '[':
                sta.append(curstr)
                sta.append(curnum)
                curstr = ""
                curnum = 0
            
            elif x == ']':
                num = sta.pop()
                prevstr = sta.pop()
                
                curstr = prevstr + curstr*num
            
            elif x.isdigit():
                
                curnum = curnum*10 + int(x)
            else:
                curstr += x
            
        return curstr
                
                
        