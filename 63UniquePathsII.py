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
        if grid[row][col] == 1:
            return 0
        if row ==0 and col ==0:
            return 1
        if (row, col) not in table:
            table[(row, col)] = self.helper(grid, table, row-1, col) + self.helper(grid, table, row, col-1)
        return table[(row, col)]

# bottom-up
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        width = len(obstacleGrid[0])
        length = len(obstacleGrid)
        
        table = [[0 for i in range(width)] for i in range(length)]
        for row in range(len(table)):
            for col in range(len(table[0])):
                if obstacleGrid[row][col] == 1:
                    table[row][col] = 0
                    continue
                if row == 0 and col == 0:
                    table[row][col] = 1
                    continue
                up = table[row-1][col] if row-1 >= 0 else 0
                left = table[row][col-1] if col-1 >=0 else 0
                table[row][col] =  up + left
        return table[-1][-1]