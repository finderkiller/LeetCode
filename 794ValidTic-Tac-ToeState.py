class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        if not board:
            return False
        rows = [0 for i in range(3)]
        cols = [0 for i in range(3)]
        diag = 0
        rev_diag = 0
        turn = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "X":
                    turn += 1
                    if row == col:
                        diag += 1
                    if row+col == 2:
                        rev_diag += 1
                    rows[col] += 1
                    cols[row] += 1
                if board[row][col] == "O":
                    turn -= 1
                    if row == col:
                        diag -= 1
                    if row+col == 2:
                        rev_diag -= 1
                    rows[col] -= 1
                    cols[row] -= 1
        xwin = rows[0]==3 or rows[1]==3 or rows[2]==3 or cols[0]==3 or cols[1]==3 or cols[2]==3 or diag==3 or rev_diag==3
        ywin = rows[0]==-3 or rows[1]==-3 or rows[2]==-3 or cols[0]==-3 or cols[1]==-3 or cols[2]==-3 or diag==-3 or rev_diag==-3
        if (turn == 0 and xwin) or (turn==1 and ywin):
            return False
        if ywin and turn == 0:
            return True
        if xwin and turn == 1:
            return True
        if turn > 1 or turn < 0:
            return False
        return True
        