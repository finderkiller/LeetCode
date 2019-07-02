#expand O(n^2)
class Result:
    def __init__(self, length, start, end):
        self.length = length
        self.start = start
        self.end = end
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlength = 0
        start = 0
        end = 0
        if s == None or len(s) == 0:
            return ""
        for idx in range(len(s)):
            result1 = self.expand(s, idx, idx)
            result2 = self.expand(s, idx, idx+1)
            if result1.length > result2.length:
                result = result1
            else:
                result = result2
            if result.length > maxlength:
                maxlength = result.length
                start = result.start
                end = result.end
        return s[start:end+1]
    def expand(self, s, left, right):
        result = Result(0, left, right)
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            result.length = right - left + 1
            result.end = right
            result.start = left
            right += 1
            left -= 1
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