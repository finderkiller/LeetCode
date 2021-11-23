"""
1. append zero for atlantic == -1 and pacific == -2
2. DFS for each coordinate, it can both reach -1 and -2

brute: O((m*n)^2)

"""
class Ret:
    def __init__(self, isAtlantic, isPacific):
        self.isAtlantic = isAtlantic
        self.isPacific = isPacific

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = [[0 for i in range(len(heights[0])+2)] for i in range(len(heights)+2)]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0:
                    grid[row][col] = -2
                elif row == len(grid)-1:
                    grid[row][col] = -1
                elif col == 0:
                    grid[row][col] = -2
                elif col == len(grid[0])-1:
                    grid[row][col] = -1
                else:
                    grid[row][col] = heights[row-1][col-1]
                    
        self.result = set()
        self.table = {}
        for row in range(1, len(grid)-1):
            for col in range(1, len(grid[0])-1):
                self.visited = set()
                self.helper(grid, row, col)           
        result = []
        for row, col in self.result:
            result.append([row-1, col-1])
        return result
        
    
    def helper(self, grid, row, col):
        if grid[row][col] == -1:
            return Ret(True, False)
        if grid[row][col] == -2:
            return Ret(False, True)
        if (row, col) in self.result:
            return Ret(True, True)
        self.visited.add((row, col))
        output = Ret(False, False)
        for next_row, next_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if grid[next_row][next_col] > grid[row][col]:
                continue
            if (next_row, next_col) in self.visited:
                continue
            forward = self.helper(grid, next_row, next_col)
            output.isAtlantic |= forward.isAtlantic
            output.isPacific |= forward.isPacific
            if output.isPacific and output.isAtlantic:
                self.result.add((row, col)) 
                break
        return output

"""
Start from boundary, BFS or DFS
"""
#time: O(m*n),
#space: O(m*n)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_point = set()
        atlantic_point = set()
        pacific_queue = []
        atlantic_queue = []
        
        for col in range(len(heights[0])):
            pacific_point.add((0, col))
            pacific_queue.append((0, col))
        
        for row in range(1, len(heights)):
            pacific_point.add((row, 0))
            pacific_queue.append((row, 0))
            
        while len(pacific_queue) > 0:
            next_queue = []
            for row, col in pacific_queue:
                for nb_row, nb_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if nb_row < 0 or nb_row == len(heights) or nb_col < 0 or nb_col == len(heights[0]):
                        continue
                    if heights[nb_row][nb_col] < heights[row][col]:
                        continue
                    if (nb_row, nb_col) in pacific_point:
                        continue
                    pacific_point.add((nb_row, nb_col))
                    next_queue.append((nb_row, nb_col))
            pacific_queue = next_queue
        for col in range(len(heights[0])):
            atlantic_point.add((len(heights)-1, col))
            atlantic_queue.append((len(heights)-1, col))
        
        for row in range(0, len(heights)-1):
            atlantic_point.add((row, len(heights[0])-1))
            atlantic_queue.append((row, len(heights[0])-1))
            
        while len(atlantic_queue) > 0:
            next_queue = []
            for row, col in atlantic_queue:
                for nb_row, nb_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if nb_row < 0 or nb_row == len(heights) or nb_col < 0 or nb_col == len(heights[0]):
                        continue
                    if heights[nb_row][nb_col] < heights[row][col]:
                        continue
                    if (nb_row, nb_col) in atlantic_point:
                        continue
                    atlantic_point.add((nb_row, nb_col))
                    next_queue.append((nb_row, nb_col))
            atlantic_queue = next_queue
        
        return list(pacific_point.intersection(atlantic_point))