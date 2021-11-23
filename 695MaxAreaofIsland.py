#DFS,
#time: O(m*n)
#space: O(m*n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    continue
                self.size = 0
                self.helper(grid, row, col)
                result = max(result, self.size)
        return result
    
    def helper(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return
        if col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == 0:
            return
        self.size += 1
        grid[row][col] = 0
        self.helper(grid, row+1, col)
        self.helper(grid, row-1, col)
        self.helper(grid, row, col+1)
        self.helper(grid, row, col-1)

#google, find max island and treat the water as island if that water area surrounded by island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #2 is not closed water
        for row in [0, len(grid)-1]:
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    self.helper(grid, row, col)
        
        for row in range(len(grid)):
            for col in [0, len(grid[0])-1]:
                if grid[row][col] == 0:
                    self.helper(grid, row, col)
                    
        # 0 is closed water
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    continue
                self.size = 0
                self.DFS(grid, row, col)
                result = max(result, self.size)
        return result
                

    def helper(self, grid, row, col):
        if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
            return
        if grid[row][col] == 1 or grid[row][col] == 2:
            return
        grid[row][col] = 2
        for next_row, next_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            self.helper(grid, next_row, next_col)
        
    def DFS(self, grid, row, col):
        if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
            return
        if grid[row][col] == 2:
            return
        grid[row][col] = 2
        self.size += 1
        for next_row, next_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            self.DFS(grid, next_row, next_col)