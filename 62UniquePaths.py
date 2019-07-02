# top-down
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = {}
        return self.helper(table, m-1, n-1)
    
    def helper(self, table, row, col):
        if row < 0 or col < 0:
            return 0
        if row == 0 and col == 0:
            return 1
        if (row, col) in table:
            return table[(row, col)]
        table[(row, col)] = self.helper(table, row-1, col) + self.helper(table, row, col-1)
        return table[(row, col)]

# bottom-up
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0 for i in range(n)] for j in range(m)]
        
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    table[0][0] = 1
                    continue
                upvalue = table[row-1][col] if row-1 >= 0 else 0
                leftvalue = table[row][col-1] if col-1 >= 0 else 0
                table[row][col] = upvalue + leftvalue
        return table[m-1][n-1]
