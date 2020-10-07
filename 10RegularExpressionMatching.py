# recursive
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.helper(s, p)
    def helper(self, s, p):
        if not p and not s:
            return True
        if not p:
            return False
        first_match = s and (p[0] == "." or s[0] == p[0])
        if len(p) >= 2 and p[1] == "*":
            return self.helper(s, p[2:]) or (first_match and self.helper(s[1:], p)) 
        return first_match and self.helper(s[1:], p[1:])
        
# memo
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.table = {}
        return self.helper(s, p)
    def helper(self, s, p):
        if s == p:
            return True
        if not p:
            return False
        if (s, p) in self.table:
            return self.table[(s, p)]
        firstmatch = s and (p[0] == "." or s[0] == p[0])
        if len(p) >= 2 and p[1] == "*":
            self.table[(s, p)] = self.helper(s, p[2:]) or (firstmatch and self.helper(s[1:], p))
            return self.table[(s, p)]
        self.table[(s, p)] = firstmatch and self.helper(s[1:], p[1:])
        return self.table[(s, p)]
        
#DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        table = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        
        table[0][0] = True
        for col in range(1,len(table[0])):
            pattern_index = col-1
            if p[pattern_index] == "*":
                table[0][col] = table[0][col-2] if col-2 >=0 else False
        
        for row in range(1,len(table)):
            for col in range(1,len(table[0])):
                string_index = row-1
                pattern_index = col-1
                if p[pattern_index] == s[string_index] or p[pattern_index] == ".":
                    table[row][col] = table[row-1][col-1]
                elif p[pattern_index] == "*":
                    table[row][col] = table[row][col-2]
                    if p[pattern_index-1] == s[string_index] or p[pattern_index-1] == ".":
                        table[row][col] |= table[row-1][col]
        return table[len(s)][len(p)]
                