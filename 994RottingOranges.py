#BFS, O(m*n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cur = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    cur.append((row, col))
        if len(cur) == 0:
            return 0 if self.isNoFresh(grid) else -1
            
        result = -1
        while len(cur) > 0:
            child = []
            for (rotten_row, rotten_col) in cur:
                if rotten_row-1 >= 0 and grid[rotten_row-1][rotten_col] == 1:
                    grid[rotten_row-1][rotten_col] = 2
                    child.append((rotten_row-1, rotten_col))
                if rotten_row+1 < len(grid) and grid[rotten_row+1][rotten_col] == 1:
                    grid[rotten_row+1][rotten_col] = 2
                    child.append((rotten_row+1, rotten_col))
                if rotten_col-1 >= 0 and grid[rotten_row][rotten_col-1] == 1:
                    grid[rotten_row][rotten_col-1] = 2
                    child.append((rotten_row, rotten_col-1))
                if rotten_col+1 < len(grid[0]) and grid[rotten_row][rotten_col+1] == 1:
                    grid[rotten_row][rotten_col+1] = 2
                    child.append((rotten_row, rotten_col+1))
            cur = child
            result += 1
        if self.isNoFresh(grid):
            return result
        else:
            return -1
    def isNoFresh(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return False
        return True