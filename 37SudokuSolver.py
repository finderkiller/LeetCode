class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.helper(board)

    def helper(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    continue
                for value in range(1, 10):
                    board[row][col] = str(value)
                    if self.isValid(board, row, col) and self.helper(board):
                        return True
                board[row][col] = "."
                return False
        return True

    def isValid(self, board, row, col):
        value = board[row][col]
        start = Coordinate(row, col)
        for col in range(len(board[0])):
            if col == start.col:
                continue
            if board[start.row][col] == value:
                return False
        for row in range(len(board)):
            if row == start.row:
                continue
            if board[row][start.col] == value:
                return False
        for row in range(start.row//3 * 3, (start.row//3+1) * 3):
            for col in range(start.col//3 * 3, (start.col//3+1) * 3):
                if row == start.row and col == start.col:
                    continue
                if board[row][col] == value:
                    return False
        return True