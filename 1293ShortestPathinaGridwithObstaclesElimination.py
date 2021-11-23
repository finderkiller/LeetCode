"""
1. BFS
2. visited_state, (x, y, remaining_removal)
3. queue[(x, y, remaining_removal)]
4. if obstacle and remaining_removal == 0, skip
"""
#time: O(m*n*k), space: O(m*n*k)
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = []
        visited = set()
        queue.append((0,0,k))
        visited.add((0,0,k))
        width = len(grid[0])
        length = len(grid)
        step = 0
        while len(queue) > 0:
            next_queue = []
            for row, col, num_removal in queue:
                if row == length-1 and col == width-1:
                    return step
                for new_row, new_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if new_row < 0 or new_row >= length or new_col < 0 or new_col >= width:
                        continue
                    if grid[new_row][new_col] == 1 and num_removal >= 1 and (new_row, new_col, num_removal-1) not in visited:
                        next_queue.append((new_row, new_col, num_removal-1))
                        visited.add((new_row, new_col, num_removal-1))
                    elif grid[new_row][new_col] == 0 and (new_row, new_col, num_removal) not in visited:
                        next_queue.append((new_row, new_col, num_removal))
                        visited.add((new_row, new_col, num_removal))
            queue = next_queue
            step += 1
        return -1