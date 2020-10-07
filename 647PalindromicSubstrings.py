#DP
class Solution(object):
    def countSubstrings(self, s):
        count = 0
        table = [[False for i in range(len(s))] for j in range(len(s))]
        for right in range(len(table)):
            for left in range(right+1):
                if left == right:
                    table[right][left] = True
                elif left+1 == right:
                    table[right][left] = s[left]==s[right]
                else:
                    table[right][left] = s[left]==s[right] and table[right-1][left+1]
                if table[right][left]:
                    count += 1
        return count
#expand
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        for idx in range(len(s)):
            self.expand(s, idx, idx)
            self.expand(s, idx, idx+1)
        return self.count
    def expand(self, s, start, end):
        while start >=0 and end < len(s) and s[start] == s[end]:
            self.count += 1
            start -=1
            end +=1        