class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if board == None:
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.': continue
                if not self.valid(board, row, col):
                    return False
        return True
    def valid(self, nums, row, col):
        value = nums[row][col]
        #! check in the row
        for j in range(len(nums[row])):
            if j == col: continue 
            if nums[row][j] == value: return False
        #! check in the col
        for i in range(len(nums)):
            if i == row: continue
            if nums[i][col] == value: return False
        #! check in the cube
        for i in range((row//3) *3, (row//3 + 1)*3):
            for j in range((col//3)*3, (col//3 + 1)*3):
                if i == row and j == col:
                    continue
                if nums[i][j] == value:
                    return False
        return True
        
        