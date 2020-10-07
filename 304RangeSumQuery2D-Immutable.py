class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.table = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for row in range(len(self.table)):
            for col in range(len(self.table[0])):
                upper = self.table[row-1][col] if row-1>=0 else 0
                left = self.table[row][col-1] if col-1>=0 else 0
                upper_left = self.table[row-1][col-1] if row-1>=0 and col-1>=0 else 0
                self.table[row][col] = matrix[row][col] + upper + left - upper_left
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        upper = self.table[row1-1][col2] if row1-1 >= 0 else 0
        left = self.table[row2][col1-1] if col1-1 >= 0 else 0
        upper_left = self.table[row1-1][col1-1] if row1-1>=0 and col1-1>=0 else 0
        return self.table[row2][col2] - upper - left + upper_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)