#memo
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        self.table = {}
        return self.helper(s, 0)
    
    def helper(self, s, start):
        if start == len(s):
            return 1
        if int(s[start]) == 0:
            return 0
        if start == len(s)-1:
            return 1
        if start in self.table:
            return self.table[start]
        result = self.helper(s, start+1)
        value = int(s[start:start+2])
        if value <= 26:
            result += self.helper(s, start+2)
        self.table[start] = result
        return result
        
#DP

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return
        table = [0 for i in range(len(s)+1)]
        table[0] = 1
        table[1] = 1 if s[0] != "0" else 0
        for idx in range(2, len(table)):
            string_idx = idx-1
            table[idx] = table[idx-1] if s[string_idx] != "0" else 0
            if s[string_idx-1] != "0" and int(s[string_idx-1:string_idx+1]) <= 26:
                table[idx] += table[idx-2]
        return table[-1]
            
