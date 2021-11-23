#memo
#time: O(s*t)
#space: O(s*t)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.table = {}
        return self.helper(s, t, 0, 0)
    def helper(self, s, t, idxs, idxt):
        if idxt == len(t):
            return 1
        if idxs == len(s):
            return 0
        if (idxs, idxt) in self.table:
            return self.table[(idxs, idxt)]
        result = 0
        if s[idxs] == t[idxt]:
            result += self.helper(s, t, idxs+1, idxt+1)
            result += self.helper(s, t, idxs+1, idxt)
        else:
            result += self.helper(s, t, idxs+1, idxt)
        self.table[(idxs, idxt)] = result
        return result

#DP
#time: O(s*t)
#space: O(s*t)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        table = [[0 for i in range(len(t)+1)] for i in range(len(s)+1)]
        for row in range(len(table)):
            table[row][-1] = 1
        for row in range(len(table)-2, -1, -1):
            for col in range(len(table[0])-2, -1, -1):
                if s[row] == t[col]:
                    table[row][col] += table[row+1][col+1]
                    table[row][col] += table[row+1][col]
                else:
                    table[row][col] += table[row+1][col]
        return table[0][0]