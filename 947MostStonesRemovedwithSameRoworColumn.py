#time: O(n), extra: O(n), depth: O(n)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if not stones:
            return 0
        self.row_table = {}
        self.col_table = {}
        self.visited = set()
        for stone in stones:
            row = stone[0]
            col = stone[1]
            if row not in self.row_table:
                self.row_table[row] = []
            self.row_table[row].append(col)
            if col not in self.col_table:
                self.col_table[col] = []
            self.col_table[col].append(row)
        self.result = 0
        for stone in stones:
            row = stone[0]
            col = stone[1]
            if (row, col) in self.visited:
                continue
            self.helper(row, col)
        return self.result
    
    def helper(self, row, col):
        self.visited.add((row, col))
        for can_col in self.row_table[row]:
            if ((row, can_col)) in self.visited:
                continue
            self.result += 1
            self.helper(row, can_col)
        for can_row in self.col_table[col]:
            if ((can_row, col)) in self.visited:
                continue
            self.result += 1
            self.helper(can_row, col)