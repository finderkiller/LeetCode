class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        queue = []
        queue.append((0, 0))
        step = 0
        width = len(grid)
        while len(queue) > 0:
            next_queue = []
            for row, col in queue:
                if row == width-1 and col == width-1:
                    return step+1
                for nb_row, nb_col in [(row+1, col), (row-1, col), \
                                       (row, col+1), (row, col-1), \
                                       (row-1, col-1), (row-1, col+1), \
                                       (row+1, col-1), (row+1, col+1)]:
                    if nb_row < 0 or nb_row == width or nb_col < 0 or nb_col == width:
                        continue
                    if grid[nb_row][nb_col] == 1 or grid[nb_row][nb_col] == 2:
                        continue
                    next_queue.append((nb_row, nb_col))
                    grid[nb_row][nb_col] = 2
            step += 1
            queue = next_queue
        return -1