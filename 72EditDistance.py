#recursive
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.helper(word1, word2)
    def helper(self, word1, word2):    
        if word1 == word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.helper(word1[1:], word2[1:])
        else:
            return min(self.helper(word1[1:], word2), self.helper(word1, word2[1:]), self.helper(word1[1:], word2[1:]))+1
#recursive, memo
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.table = {}
        return self.helper(word1, word2)
    def helper(self, word1, word2):    
        if word1 == word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if (word1, word2) in self.table:
            return self.table[(word1, word2)]
        if word1[0] == word2[0]:
            self.table[(word1, word2)] = self.helper(word1[1:], word2[1:])
            return self.table[(word1, word2)]
        else:
            self.table[(word1, word2)] = min(self.helper(word1[1:], word2), self.helper(word1, word2[1:]), self.helper(word1[1:], word2[1:]))+1
            return self.table[(word1, word2)]
#DP
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
        