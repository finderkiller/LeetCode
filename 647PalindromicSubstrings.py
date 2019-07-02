#DP
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        table = [[False for i in range(len(s))] for j in range(len(s))]
        for right in range(len(table)):
            table[right][right] = True
            count += 1
            for left in range(len(table[0])):
                if left+1 == right and s[left] == s[right]:
                    table[right][left] = True
                    count +=1
                if left+1 < right and s[left] == s[right] and table[right-1][left+1]:
                    table[right][left] = True
                    count +=1
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