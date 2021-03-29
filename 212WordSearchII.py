class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        self.result = []
        
        for word in words:
            found = False
            for row in range(len(board)):
                for col in range(len(board[0])):
                    self.visited = set()
                    if self.helper(word, 0, row, col, board):
                        self.result.append(word)
                        found = True
                        break
                if found:
                    break
                        
        return self.result
                    
    def helper(self, word, start, row, col, board):
        if row < 0 or row == len(board):
            return False
        if col < 0 or col == len(board[0]):
            return False
        if (row, col) in self.visited:
            return False
        if start == len(word)-1 and board[row][col] == word[start]:
            return True
        if board[row][col] != word[start]:
            return False
        self.visited.add((row, col))
        result = self.helper(word, start+1, row+1, col, board) or self.helper(word, start+1, row-1, col, board) or self.helper(word, start+1, row, col+1, board) or self.helper(word, start+1, row, col-1, board)
        self.visited.remove((row, col))
        return result