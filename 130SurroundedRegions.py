class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or row == len(board)-1 or col == 0 or col == len(board[0])-1) and board[row][col] == "O":
                    self.fillBorder(board, row, col, "O", "Y")
        self.replace(board)

    def fillBorder(self, board, row, col, target, char):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return
        if board[row][col] != target:
            return 
        board[row][col] = char
        self.fillBorder(board, row-1, col, target, char)
        self.fillBorder(board, row+1, col, target, char)
        self.fillBorder(board, row, col-1, target, char)
        self.fillBorder(board, row, col+1, target, char)
    def replace(self, board):
        if not board:
            return
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "Y":
                    board[row][col] = "O"


#BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or row == len(board)-1 or col == 0 or col == len(board[0])-1) and board[row][col] == "O":
                    self.fillBorder(board, row, col, "O", "Y")
        self.replace(board)

    def fillBorder(self, board, row, col, target, char):
        queue = [(row, col)]
        while len(queue) > 0:
            coordinate = queue.pop()
            row = coordinate[0]
            col = coordinate[1]
            board[row][col] = char
            if row > 0 and board[row-1][col] == target:
                queue.append((row-1, col))
            if row < len(board)-1 and board[row+1][col] == target:
                queue.append((row+1, col))
            if col > 0 and board[row][col-1] == target:
                queue.append((row, col-1))
            if col < len(board[0]) -1 and board[row][col+1] == target:
                queue.append((row, col+1))
            
    def replace(self, board):
        if not board:
            return
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "Y":
                    board[row][col] = "O"