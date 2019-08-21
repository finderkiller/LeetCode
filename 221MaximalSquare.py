#DP, using 2 dimension array
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        table = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        max_length = 0
        for row in range(len(table)):
            for col in range(len(table[0])):
                if row == 0 or col == 0:
                    table[row][col] = int(matrix[row][col])
                elif matrix[row][col] == "0":
                    table[row][col] = 0
                else:
                    table[row][col] = min(table[row-1][col-1], table[row-1][col], table[row][col-1]) + 1
                max_length = max(max_length, table[row][col])
        return max_length * max_length
                