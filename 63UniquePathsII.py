# top-down
# #time: O(m*n), space: O(m*n), depth: O(m+n)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.table = {}
        return self.helper(obstacleGrid, len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        
    def helper(self, obstacleGrid, row, col):
        if row < 0 or col < 0:
            return 0
        if obstacleGrid[row][col] == 1:
            return 0
        if row == 0 and col == 0:
            return 1
        if (row, col) in self.table:
            return self.table[(row, col)]
        self.table[(row, col)] = self.helper(obstacleGrid, row-1, col) + self.helper(obstacleGrid, row, col-1)
        return self.table[(row, col)]

# bottom-up
#time: O(m*n), space: O(m*n)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        table = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        for row in range(len(table)):
            for col in range(len(table[0])):
                if obstacleGrid[row][col] == 1:
                    table[row][col] = 0
                elif row == 0 and col == 0:
                    table[row][col] = 1
                else:
                    up = table[row-1][col] if row-1 >=0 else 0
                    left = table[row][col-1] if col-1 >=0 else 0
                    table[row][col] = up + left
        return table[-1][-1]