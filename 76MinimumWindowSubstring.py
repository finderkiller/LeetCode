class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        if not s or not t:
            return ""
        left = 0
        right = 0
        table = self.buildTable(t)
        result = ""
        min_length = sys.maxsize
        count = 0
        while right < len(s):
            table[s[right]] = table.get(s[right], 0)-1
            if table[s[right]] >=0:
                count += 1
            while count == len(t):
                if right-left+1 < min_length:
                    min_length = right-left+1
                    result = s[left:right+1]
                table[s[left]] = table.get(s[left], 0)+1
                if table[s[left]] > 0:
                    count -= 1
                left += 1
            right += 1
        return result
            
            
    def buildTable(self, string):
        table = {}
        for char in string:
            table[char] = table.get(char, 0)+1
        return table