#brute force, time: O(m*n) for on move, space: O(1)
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.table = [[None for i in range(n)] for i in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if row >= len(self.table) or row < 0 or col >= len(self.table) or col <0:
            return 0
        self.table[row][col] = "X" if player ==1 else "O"
        if self.checkWin(row, col, "X" if player ==1 else "O"):
            return player
        return 0
        
    def checkWin(self, row, col, char):
        connection = True
        if row + col == self.n - 1:
            for row_idx in range(len(self.table)):
                for col_idx in range(len(self.table)):
                    if row_idx + col_idx != self.n - 1:
                        continue
                    if self.table[row_idx][col_idx] != char:
                        connection = False
                        break
            if connection:
                return True
        connection = True
        if row == col:
            for row_idx in range(len(self.table)):
                for col_idx in range(len(self.table)):
                    if row_idx != col_idx:
                        continue
                    if self.table[row_idx][col_idx] != char:
                        connection = False
                        break
            if connection:
                return True
        connection = True
        for col_idx in range(len(self.table)):
            if self.table[row][col_idx] != char:
                connection = False
                break
        if connection:
            return True
        
        connection = True
        for row_idx in range(len(self.table)):
            if self.table[row_idx][col] != char:
                connection = False
                break
        return connection
    
#time: O(1) for one move, O(n) for n trail, space: O(m+n)
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.diag = 0
        self.rev_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if row >= self.n or row < 0 or col >= self.n or col <0:
            return 0
        delta = 1 if player == 1 else -1
        self.rows[col] += delta
        self.cols[row] += delta
        if row == col:
            self.diag += delta
        if row+col == self.n-1:
            self.rev_diag += delta
        if abs(self.rows[col]) == self.n or abs(self.cols[row]) == self.n or abs(self.diag) == self.n or abs(self.rev_diag) == self.n:
            return player
        return 0