class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        table = {}
        for char in secret:
            if char not in table:
                table[char] = 0
            table[char] += 1
        
        for idx in range(len(guess)):
            if guess[idx] == secret[idx]:
                bulls += 1
                table[guess[idx]] -= 1
        
        for idx in range(len(guess)):
            if guess[idx] == secret[idx]:
                continue      
            if guess[idx] in table and table.get(guess[idx]) > 0:
                cows += 1
                table[guess[idx]] -= 1
        
        return "{0}A{1}B".format(bulls, cows)