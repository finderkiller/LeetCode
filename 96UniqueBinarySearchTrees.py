# memo
class Solution:
    def numTrees(self, n: int) -> int:
        table = {}
        return self.helper(1, n, table)
    
    def helper(self, start, end, table):
        if start > end:
            return 1
        if (start, end) in table:
            return table[(start, end)]
        result = 0
        for value in range(start, end+1):
            left = self.helper(start, value-1, table)
            right = self.helper(value+1, end, table)
            result += left * right
        table[(start, end)] = result
        return result

# memo, 不用start end
class Solution:
    def numTrees(self, n: int) -> int:
        table = {}
        return self.helper(n, table)
    
    def helper(self, n, table):
        if n == 0:
            return 1
        if n in table:
            return table[n]
        result = 0
        for idx in range(n):
            left = self.helper(idx, table)
            right = self.helper(n-1-idx, table)
            result += left * right
        table[n] = result
        return result

# bottom-up
class Solution:
    def numTrees(self, n: int) -> int:
        table = [0 for idx in range(n+1)]
        table[0] = 1
        for idx in range(1, n+1):
            for idj in range(idx):
                table[idx] += table[idj] * table[idx-1-idj]
        return table[n]