#time: O(m*n)
#space: O(m*n)
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return []
        result = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    continue
                self.collection = []
                self.helper(grid, row, col, row, col)
                result.add(tuple(self.collection))
        return len(result)
        
    def helper(self, grid, row, col, ori_row, ori_col):
        if row < 0 or row >= len(grid):
            return
        if col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == 0:
            return
        grid[row][col] = 0
        self.collection.append((row-ori_row, col-ori_col))
        self.helper(grid, row-1, col, ori_row, ori_col)
        self.helper(grid, row+1, col, ori_row, ori_col)
        self.helper(grid, row, col-1, ori_row, ori_col)
        self.helper(grid, row, col+1, ori_row, ori_col)