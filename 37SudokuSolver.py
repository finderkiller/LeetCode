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
                    if self.valid(board, row, col, str(value)):
                        board[row][col] = str(value)
                        if self.helper(board):
                            return True
                board[row][col] = "."
                return False
        return True
                    
    def valid(self, board, input_row, input_col, value):
        for col in range(len(board[0])):
            if board[input_row][col] == value:
                return False
        for row in range(len(board)):
            if board[row][input_col] == value:
                return False
        for row in range((input_row//3)*3, (input_row//3 + 1)*3):
            for col in range((input_col//3)*3, (input_col//3 + 1)*3):
                if board[row][col] == value:
                    return False
        return True