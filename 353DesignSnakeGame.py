#space: O(W*H+N), time for move: O(1)

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.hash_set = set()
        self.hash_set.add((0, 0))
        self.queue = collections.deque([(0, 0)])
        self.food = food
        self.food_idx = 0
        self.size = 0
        

    def move(self, direction: str) -> int:
        cur_row, cur_col = self.queue[-1]
        if direction == "U":
            cur_row -= 1
        elif direction == "D":
            cur_row += 1
        elif direction == "L":
            cur_col -= 1
        elif direction == "R":
            cur_col += 1
        if cur_row < 0 or cur_row == self.height:
            return -1
        if cur_col < 0 or cur_col == self.width:
            return -1
        if self.food_idx < len(self.food) and \
            cur_row == self.food[self.food_idx][0] and cur_col == self.food[self.food_idx][1]:
            self.queue.append((cur_row, cur_col))
            self.hash_set.add((cur_row, cur_col))
            self.food_idx += 1
            self.size += 1
        else:
            self.hash_set.remove(self.queue[0])
            self.queue.popleft()
            if (cur_row, cur_col) in self.hash_set:
                return -1
            self.queue.append((cur_row, cur_col))
            self.hash_set.add((cur_row, cur_col))
        return self.size