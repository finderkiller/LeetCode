"""
1. find row, col
2. traverse string
    get difference of row and col between cur_row, cur_col, append to result
    cur_row = row,
    cur_col = col,
3. return result
test:
1. l e e t
l:
    cur_row = 0
    cur_col = 4
    row = 0
    col = 4
    diff_row = 0
    diff_col = 0
    
result = "DDR!UURRR!!"


"""
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        cur_row = 0
        cur_col = 0
        result = ""
        for char in target:
            row, col = self.getRowCol(char)
            diff_row = row-cur_row
            diff_col = col-cur_col
            #handle target == zdz, if row == 5, meaning only move L and D, and move L first
            if row == 5:
                diff_col = abs(diff_col)
                while diff_col > 0:
                    result += "L"
                    diff_col -= 1
                while diff_row > 0:
                    result += "D"
                    diff_row -= 1
            else:
                if diff_row > 0:
                    while diff_row > 0:
                        result += "D"
                        diff_row -= 1
                elif diff_row < 0:
                    diff_row = abs(diff_row)
                    while diff_row > 0:
                        result += "U"
                        diff_row -= 1
                if diff_col > 0:
                    while diff_col > 0:
                        result += "R"
                        diff_col -= 1
                elif diff_col < 0:
                    diff_col = abs(diff_col)
                    while diff_col > 0:
                        result += "L"
                        diff_col -= 1
            result += "!"
            cur_row = row
            cur_col = col
        return result
        
    def getRowCol(self, char):
        diff = ord(char) - ord('a')
        row = diff//5
        col = diff%5
        return (row, col)