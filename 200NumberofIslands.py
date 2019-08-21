class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    result += 1
                    self.helper(grid, row, col)
        return result
    def helper(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
            return
        grid[row][col] = "0"
        self.helper(grid, row+1, col)
        self.helper(grid, row-1, col)
        self.helper(grid, row, col+1)
        self.helper(grid, row, col-1)
        