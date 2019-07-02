class Solution:
    def numDecodings(self, s: str) -> int:
        table = {}
        return self.helper(s, table)
    def helper(self, s, table):
        if not s:
            return 1
        if s[0] == "0":
            return 0
        if s in table:
            return table[s]
        result = 0
        if len(s) >= 2 and int(s[0:2]) <= 26:
            result += self.numDecodings(s[2:])
        result += self.numDecodings(s[1:])
        table[s] = result
        return table[s]
        

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0] == "0":
            return 0
        string = s[::-1]
        table = [0 for i in range(len(s) + 1)]
        table[0] = 1
        
        for idx in range(1, len(table)):
            if string[idx-1:idx] == "0":
                continue
            table[idx] += table[idx-1]
            if idx < 2:
                continue
            char_two = string[idx-2:idx]
            
            if int(char_two[::-1]) <= 26:
                table[idx] += table[idx-2]
        return table[len(s)]
            
