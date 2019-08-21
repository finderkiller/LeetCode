class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True
        return self.validRow(board) and self.validCol(board) and self.validCube(board)
    def validRow(self, board):
        for row in range(len(board)):
            table = set()
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in table:
                    return False
                table.add(board[row][col])
        return True
    def validCol(self, board):
        for col in range(len(board[0])):
            table= set()
            for row in range(len(board)):
                if board[row][col] == ".":
                    continue
                if board[row][col] in table:
                    return False
                table.add(board[row][col])
        return True
    def validCube(self, board):
        for i in range(len(board)//3):
            for j in range(len(board)//3):
                table = set()
                for row in range(i*3, (i+1)*3):
                    for col in range(j*3, (j+1)*3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in table:
                            return False
                        table.add(board[row][col])
        return True
        
            
            
        