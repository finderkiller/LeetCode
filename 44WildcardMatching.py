#recursive, memo
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        pattern = ""
        for idx in range(len(p)):
            if idx > 0 and p[idx] == "*" and p[idx-1] == "*":
                continue
            pattern += p[idx]
        self.table = {}
        return self.helper(s, pattern)
    def helper(self, s, p):
        if s == p:
            return True
        if not p:
            return False
        if (s, p) in self.table:
            return self.table[(s, p)]
        firstmatch = s and (p[0] == "?" or p[0] == "*" or s[0] == p[0])
        if p[0] == "*":
            self.table[(s, p)] = self.helper(s, p[1:]) or (firstmatch and self.helper(s[1:], p))
            return self.table[(s, p)]
        self.table[(s, p)] = firstmatch and self.helper(s[1:], p[1:])
        return self.table[(s, p)]
#DP
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not p:
            return False
        table = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        table[0][0] = True
        for col in range(1, len(table[0])):
            p_idx = col-1
            if p[p_idx] == "*":
                table[0][col] = table[0][col-1]
        
        for row in range(1, len(table)):
            for col in range(1, len(table[0])):
                p_idx = col-1
                s_idx = row-1
                if p[p_idx] == "?" or p[p_idx] == s[s_idx]:
                    table[row][col] = table[row-1][col-1]
                elif p[p_idx] == "*":
                    table[row][col] = table[row][col-1]
                    table[row][col] |= table[row-1][col]
        return table[-1][-1]