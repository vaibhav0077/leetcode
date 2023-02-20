class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        cows = 0
        bulls = 0
        guess = list(guess)
        freq = [0 for i in range(10)]
        for i in range(n):
            if secret[i] == guess[i]: 
                bulls+=1
                guess[i] = "-1"
            
            else:
                freq[int(secret[i])]+=1
        
        for i in range(n):
            if guess[i] !="-1":
                
                if freq[int(guess[i])] > 0:
                    cows+=1
                    freq[int(guess[i])] -= 1
        
        
        return  str(bulls) + "A" + str(cows) + "B"
            
            
        