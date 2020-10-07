class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return
        collect = []
        result = []
        self.helper(0, n, collect, result)
        return result
    def helper(self, row, size, collect, result):
        if row == size:
            result.append(self.genMap(collect))
            return
        for col in range(size):
            if not self.isValid(collect, row, col):
                continue
            collect.append(col)
            self.helper(row+1, size, collect, result)
            collect.pop()
                
    def isValid(self, collect, new_row, new_col):
        for row, col in enumerate(collect):
            if col == new_col:
                return False
            row_diff = abs(new_row-row)
            col_diff = abs(new_col-col)
            if row_diff == col_diff:
                return False
        return True
    def genMap(self, collect):
        ret = []
        for col in collect:
            row_value = ["." for i in range(len(collect))]
            row_value[col] = "Q"
            ret.append("".join(row_value))
        return ret