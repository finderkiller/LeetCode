"""
[1,0,2,0,1]
[0,0,0,0,0]
[0,0,1,0,0]

brute force: find each empty place and calculate the distance
O(m*n * m*n), for each element and BFS find the target



"""

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        min_distance = sys.maxsize
        building_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    building_count += 1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    continue
                result = self.BFS(grid, row, col, building_count)
                if result != -1:
                    min_distance = min(min_distance, result)
        return min_distance if min_distance != sys.maxsize else -1
                    
    def BFS(self, grid, start_row, start_col, building_count):
        queue = []
        queue.append((start_row, start_col))
        visited = set()
        visited.add((start_row, start_col))
        step = 0
        result = 0
        row_length = len(grid)
        col_length = len(grid[0])
        while len(queue) > 0:
            next_level = []
            step += 1
            for row, col in queue:
                if row+1 < row_length and (row+1, col) not in visited:
                    visited.add((row+1, col))
                    if grid[row+1][col] == 1:
                        result += step
                        building_count -= 1
                    elif grid[row+1][col] == 0 :
                        next_level.append((row+1, col))
                if row-1 >= 0 and (row-1, col) not in visited:
                    visited.add((row-1, col))
                    if grid[row-1][col] == 1:
                        result += step
                        building_count -= 1
                    elif grid[row-1][col] == 0 :
                        next_level.append((row-1, col))
                if col+1 < col_length and (row, col+1) not in visited:
                    visited.add((row, col+1))
                    if grid[row][col+1] == 1:
                        result += step
                        building_count -= 1
                    elif grid[row][col+1] == 0 :
                        next_level.append((row, col+1))
                if col-1 >= 0 and (row, col-1) not in visited:
                    visited.add((row, col-1))
                    if grid[row][col-1] == 1:
                        result += step
                        building_count -= 1
                    elif grid[row][col-1] == 0 :
                        next_level.append((row, col-1))
            queue = next_level
        return result if building_count == 0 else -1
            
                
                