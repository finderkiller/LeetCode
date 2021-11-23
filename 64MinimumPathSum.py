# top-down
# time: O(m*n), space: O(m*n), depth: O(m+n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.table = {}
        return self.helper(grid, len(grid)-1, len(grid[0])-1)
        
    def helper(self, grid, row, col):
        if row < 0 or col < 0:
            return sys.maxsize
        if row == 0 and col == 0:
            return grid[row][col]
        if (row, col) in self.table:
            return self.table[(row, col)]
        self.table[(row, col)] = grid[row][col]
        self.table[(row, col)] += min(self.helper(grid, row-1, col), self.helper(grid, row, col-1))
        return self.table[(row, col)]

# bottom-up
# # time: O(m*n), space: O(m*n) 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        table = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        for row in range(len(table)):
            for col in range(len(table[0])):
                if row == 0 and col == 0:
                    table[row][col] = grid[row][col]
                else:
                    up = table[row-1][col] if row-1 >=0 else sys.maxsize
                    left = table[row][col-1] if col-1 >=0 else sys.maxsize
                    table[row][col] = min(up, left) + grid[row][col]
        return table[-1][-1]
