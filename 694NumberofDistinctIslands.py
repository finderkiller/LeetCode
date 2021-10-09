class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return []
        uniq_island = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    continue
                self.collect = set()
                self.helper(grid, row, col, row, col)
                uniq_island.add(frozenset(self.collect))
        return len(uniq_island)
    
    def helper(self, grid, row, col, ori_row, ori_col):
        if row < 0 or row >= len(grid):
            return
        if col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == 0:
            return
        grid[row][col] = 0
        self.collect.add((row-ori_row, col-ori_col))
        self.helper(grid, row+1, col, ori_row, ori_col)
        self.helper(grid, row-1, col, ori_row, ori_col)
        self.helper(grid, row, col+1, ori_row, ori_col)
        self.helper(grid, row, col-1, ori_row, ori_col)