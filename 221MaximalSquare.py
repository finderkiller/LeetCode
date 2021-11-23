#DP, using 2 dimension array
#time: O(n^2), space: O(n^2)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        table = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        max_length = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    continue
                elif row == 0 or col == 0:
                    table[row][col] = 1
                else:
                    table[row][col] = min(table[row-1][col-1], table[row-1][col], table[row][col-1]) + 1
                max_length = max(max_length, table[row][col])
        return max_length**2
                