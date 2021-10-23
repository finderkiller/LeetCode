#time: O(m*n*3^L), m rows, n cols, L words length, depth: O(L)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        height = len(board)
        width = len(board[0])
        for row in range(height):
            for col in range(width):
                if (self.helper(board, height, width, row, col, word)):
                    return True
        return False
        
    
    def helper(self, board, height, width, row, col, word):
        if len(word) == 0:
            return True
        if row >= height or row < 0:
            return False
        if col >= width or col < 0:
            return False
        if board[row][col] != word[0]:
            return False
        char = board[row][col]
        board[row][col] = '-'
        result = self.helper(board, height, width, row-1, col, word[1:]) or self.helper(board, height, width, row+1, col, word[1:]) or self.helper(board, height, width, row, col-1, word[1:]) or self.helper(board, height, width, row, col+1, word[1:])
        board[row][col] = char
        return result