class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        table = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        for col in range(len(table[0])):
            table[0][col] = col
        for row in range(len(table)):
            table[row][0] = row
        for row in range(1,len(table)):
            for col in range(1, len(table[0])):
                table[row][col] = min(table[row-1][col]+1, table[row][col-1]+1, table[row-1][col-1]+1 if word2[row-1] != word1[col-1] else table[row-1][col-1])
        return table[-1][-1]
        