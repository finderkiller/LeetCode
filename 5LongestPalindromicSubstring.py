#expand O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        result = ""
        for idx in range(len(s)):
            a = self.expand(s, idx, idx)
            b = self.expand(s, idx, idx+1)
            if len(result) < len(a):
                result = a
            if len(result) < len(b):
                result = b
        return result
            
    def expand(self, string, left, right):
        result = ""
        while left >=0 and right < len(string) and string[left]==string[right]:
            result = string[left:right+1]
            left-=1
            right+=1
        return result
#DP O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        table = [[0 for i in range(len(s))] for j in range(len(s))]
        max_length = 0
        start = 0
        end = 0
        for right in range(len(table)):
            table[right][right] = True
            for left in range(0, right):
                if left+1 == right:
                    table[right][left] = s[left] == s[right]
                if left+1 < right:
                    table[right][left] = s[left] == s[right] and table[right-1][left+1]
                if table[right][left] and right-left+1 > max_length:
                    start = left
                    end = right
                    max_length = right-left+1
        return s[start:end+1]     