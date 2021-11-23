#DFS O(m*n), depth: O(m*n), extra: O(m*n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        result = 0
        self.visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    result += 1
                    self.helper(grid, row, col)
        return result
    def helper(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return
        if grid[row][col] == "0":
            return
        if (row, col) in self.visited:
            return
        self.visited.add((row, col))
        self.helper(grid, row+1, col)
        self.helper(grid, row-1, col)
        self.helper(grid, row, col+1)
        self.helper(grid, row, col-1)

#DFS O(m*n), depth: O(m*n)
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

#BFS, O(m*n), space: O(w), depends queue's length
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        result = 0
        queue = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '0':
                    continue
                result += 1
                grid[row][col] = '0'
                queue.append((row, col))
                while queue:
                    cur_row, cur_col = queue.pop()
                    if cur_row + 1 < len(grid) and grid[cur_row+1][cur_col] == '1':
                        grid[cur_row+1][cur_col] = '0'
                        queue.append((cur_row+1, cur_col))
                    if cur_row - 1 >= 0 and grid[cur_row-1][cur_col] == '1':
                        grid[cur_row-1][cur_col] = '0'
                        queue.append((cur_row-1, cur_col))
                    if cur_col + 1 < len(grid[0]) and grid[cur_row][cur_col+1] == '1':
                        grid[cur_row][cur_col+1] = '0'
                        queue.append((cur_row, cur_col+1))
                    if cur_col - 1 >= 0 and grid[cur_row][cur_col-1] == '1':
                        grid[cur_row][cur_col-1] = '0'
                        queue.append((cur_row, cur_col-1))
        return result
        