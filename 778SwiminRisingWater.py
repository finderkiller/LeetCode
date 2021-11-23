#brute Force
#DFS find every path and find the maximum for each path, 
#minmum with each maximum, difference with (0,0) is the answer

#heap
#time: O(n^2*logn)
#space: O(n)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        length = width = len(grid)
        import heapq
        min_heap = []
        min_heap.append((grid[0][0], 0, 0))
        max_height = 0
        visited = set()
        
        while len(min_heap) > 0:
            height, row, col = heapq.heappop(min_heap)
            max_height = max(max_height, height)
            if row == col == length-1:
                return max_height
            for nb_row, nb_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if nb_row < 0 or nb_row == length or nb_col < 0 or nb_col == width:
                    continue
                if (nb_row, nb_col) in visited:
                    continue
                heapq.heappush(min_heap, (grid[nb_row][nb_col], nb_row, nb_col))
                visited.add((nb_row, nb_col))
        return 0