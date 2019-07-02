# top-down<F5>
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        table = {}
        return self.helper(grid, table, len(grid)-1, len(grid[0])-1)
    
    def helper(self, grid, table, row, col):
        if row < 0 or col <0:
            return sys.maxsize
        if row == 0 and col == 0:
            return grid[0][0]
        if (row, col) in table:
            return table[(row, col)]
        
        table[(row, col)] = grid[row][col] + min(self.helper(grid, table, row-1, col), self.helper(grid, table, row, col-1))
        return table[(row, col)]

# bottom-up
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        table = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    table[0][0] = grid[0][0]
                    continue
                valueup = table[row-1][col] if row-1 >= 0 else sys.maxsize
                valueleft = table[row][col-1] if col-1 >=0 else sys.maxsize
                table[row][col] = grid[row][col] + min(valueup, valueleft)
        return table[len(grid)-1][len(grid[0])-1]
