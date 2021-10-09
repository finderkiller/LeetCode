class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        if len(grid[0]) == 0:
            return 0
        area = {}
        index = 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    index += 1
                    area[index] = self.helper(grid, row, col, index)
        area[0] = 0
        result = max(area.values())
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    continue
                area_set = set()
                cur_area = 1
                area_set.add(grid[row][col-1] if col-1 >= 0 else 0)
                area_set.add(grid[row][col+1] if col+1 < len(grid[0]) else 0)
                area_set.add(grid[row-1][col] if row-1 >= 0 else 0)
                area_set.add(grid[row+1][col] if row+1 < len(grid) else 0)
                for idx in area_set:
                    cur_area += area[idx]
                result = max(result, cur_area)
        return result
                    
    def helper(self, grid, row, col, index):
        if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
            return 0
        if grid[row][col] != 1:
            return 0
        result = 1
        grid[row][col] = index
        result += self.helper(grid, row-1, col, index)
        result += self.helper(grid, row+1, col, index)
        result += self.helper(grid, row, col-1, index)
        result += self.helper(grid, row, col+1, index)
        return result