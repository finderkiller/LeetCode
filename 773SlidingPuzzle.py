class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        queue = []
        visited = set()
        target = "123450"
        start = ""
        directions = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                start += str(board[row][col])
                
        queue.append(start)
        visited.add(start)
        step = 0
        while len(queue) > 0:
            next_queue = []
            for status in queue:
                if status == target:
                    return step
                zero_index = status.find('0')
                for direction in directions[zero_index]:
                    status_array = list(status)
                    status_array[zero_index] = status_array[direction]
                    status_array[direction] = '0'
                    next_status = ''.join(status_array)
                    if next_status in visited:
                        continue
                    next_queue.append(next_status)
                    visited.add(next_status)
            queue = next_queue
            step += 1
        return -1