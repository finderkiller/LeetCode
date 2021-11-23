"""
1. find 0 groups, and exclude when touch edge

"""
#DFS, time: O(m*n), depth: O(m*n), space: O(m*n), remember to reset island to water after getting False from next_node
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0
        self.visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 or (row, col) in self.visited:
                    continue
                if self.helper(grid, row, col):
                    result += 1
        return result
                
    def helper(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        if grid[row][col] == 1:
            return True
        if (row, col) in self.visited:
            return True
        self.visited.add((row, col))
        if not self.helper(grid, row+1, col):
            self.visited.remove((row, col))
            return False
        if not self.helper(grid, row-1, col):
            self.visited.remove((row, col))
            return False
        if not self.helper(grid, row, col+1):
            self.visited.remove((row, col))
            return False
        if not self.helper(grid, row, col-1):
            self.visited.remove((row, col))
            return False
        return True

#DFS, time: O(m*n), depth: O(m*n), remember to reset island to water after getting False from next_node
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    continue
                if self.helper(grid, row, col):
                    result += 1
        return result
                
    def helper(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        if grid[row][col] == 1:
            return True
        grid[row][col] = 1
        if not self.helper(grid, row+1, col):
            grid[row][col] = 0
            return False
        if not self.helper(grid, row-1, col):
            grid[row][col] = 0
            return False
        if not self.helper(grid, row, col+1):
            grid[row][col] = 0
            return False
        if not self.helper(grid, row, col-1):
            grid[row][col] = 0
            return False
        return True

#DFS, flip land to water for the land which connect with boards
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        for row in [0, len(grid)-1]:
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    self.filpToWater(grid, row, col)
        
        for row in range(len(grid)):
            for col in [0, len(grid[0])-1]:
                if grid[row][col] == 0:
                    self.filpToWater(grid, row, col)
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    continue
                self.filpToWater(grid, row, col)
                result +=1
        return result
                

    def filpToWater(self, grid, row, col):
        if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
            return
        if grid[row][col] == 1:
            return
        grid[row][col] = 1
        for next_row, next_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            self.filpToWater(grid, next_row, next_col)

#google, find the largest closedIsland
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0
        self.visited = set()
        max_island = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 or (row, col) in self.visited:
                    continue
                self.size = 0
                if self.helper(grid, row, col):
                    max_island = max(max_island, self.size)
                    result += 1
        print(max_island)
        return result
                
    def helper(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        if grid[row][col] == 1:
            return True
        if (row, col) in self.visited:
            return True
        self.size += 1
        self.visited.add((row, col))
        if not self.helper(grid, row+1, col):
            self.visited.remove((row, col))
            return False
        if not self.helper(grid, row-1, col):
            self.visited.remove((row, col))
            return False
        if not self.helper(grid, row, col+1):
            self.visited.remove((row, col))
            return False
        if not self.helper(grid, row, col-1):
            self.visited.remove((row, col))
            return False
        return True