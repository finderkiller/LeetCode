class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        first_row_has_zero = False
        first_col_has_zero = False
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                first_row_has_zero = True
                break
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                first_col_has_zero = True
                break
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                matrix[row] = [0 for i in range(len(matrix[0]))]
        
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
        
        if first_row_has_zero:
            matrix[0] = [0 for i in range(len(matrix[0]))]
        if first_col_has_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0 