# top-down
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        width = len(obstacleGrid[0])
        length = len(obstacleGrid)
        table = {}
        if obstacleGrid[length-1][width-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        return self.helper(obstacleGrid, table, length-1, width-1)
    
    def helper(self, grid, table, row, col):
        if row < 0 or col < 0:
            return 0
        if row ==0 and col ==0:
            return 1
        if grid[row][col] == 1:
            return 0
        if (row, col) in table:
            return table[(row, col)]
        table[(row, col)] = self.helper(grid, table, row-1, col) + self.helper(grid, table, row, col-1)
        return table[(row, col)]

# bottom-up
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        width = len(obstacleGrid[0])
        length = len(obstacleGrid)
        if obstacleGrid[length-1][width-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        table = [[0 for i in range(width)] for j in range(length)]
        
        for row in range(length):
            for col in range(width):
                if row == 0 and col == 0:
                    table[0][0] = 1
                    continue
                if obstacleGrid[row][col] == 1:
                    table[row][col] = 0
                    continue
                upvalue = table[row-1][col] if row-1>=0 else 0
                leftvalue = table[row][col-1] if col-1>=0 else 0
                table[row][col] = upvalue + leftvalue
        return table[length-1][width-1] 
