class Solution:
    def fib(self, n):
        
        if(n == 0):
            return n
        if(n == 1):
            return 1
        
        a = 1
        b = 1
        
        for i in range(2,n):
            fib = a + b
            a = b
            b = fib
            
            
        return b;