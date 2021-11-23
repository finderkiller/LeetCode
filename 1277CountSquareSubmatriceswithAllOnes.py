#time: O(n^2), space: O(n^2)
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0
        table = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    table[row][col] = 0
                elif row == 0 or col == 0:
                    table[row][col] = 1 
                else:
                    table[row][col] = min(table[row-1][col-1], table[row-1][col], table[row][col-1])+1
                result += table[row][col]
        return result