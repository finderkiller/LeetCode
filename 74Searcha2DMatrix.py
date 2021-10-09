# rightup-to-leftdown Time:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        col = len(matrix[0])-1
        row = 0
        while col >= 0 and row < len(matrix):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

# rightup-to-leftdown recursive
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        return self.helper(matrix, 0, len(matrix[0])-1, target)
        
    def helper(self, matrix, row, col, target):
        if row >= len(matrix) or col < 0:
            return False
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            return self.helper(matrix, row+1, col, target)
        else:
            return self.helper(matrix, row, col-1, target)

#對角線的binary search
class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def isbefore(self, point):
        return self.row <= point.row and self.col <= point.col
    def average(self, p1, p2):
        self.row = p1.row + (p2.row-p1.row)//2
        self.col = p1.col + (p2.col-p1.col)//2
    def inbound(self, matrix):
        width = len(matrix[0])
        height = len(matrix)
        return 0 <= self.row and self.row < height and 0 <= self.col and self.col < width
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        width = len(matrix[0])
        height = len(matrix)
        return self.helper(matrix, Coordinate(0,0), Coordinate(height-1, width-1), target)
    def helper(self, matrix, start, end, target):
        if not start.inbound(matrix) or not end.inbound(matrix):
            return False

        if (not start.isbefore(end)):
            return False

        dist = min(end.row-start.row, end.col-start.col)
        pstart = Coordinate(start.row, start.col)   
        pend = Coordinate(start.row + dist, end.row + dist)
        mid = Coordinate(0,0)
        while pstart.isbefore(pend):
            mid.average(pstart, pend)
            if matrix[mid.row][mid.col] == target:
                return True
            elif matrix[mid.row][mid.col] < target:
                pstart.row = mid.row+1
                pstart.col = mid.col+1
            else:
                pend.row = mid.row-1
                pend.col = mid.col-1
        return self.partition(matrix, start, end, pstart, target)
    def partition(self, matrix, start, end, pstart, target):
        leftdownstart = Coordinate(pstart.row, start.col)
        leftdowend = Coordinate(end.row, pstart.col-1)
        rightupstart = Coordinate(start.row, pstart.col)
        rightupend = Coordinate(pstart.row-1,end.col)
        
        result = self.helper(matrix, leftdownstart, leftdowend, target)
        if not result:
            result = self.helper(matrix, rightupstart, rightupend, target)
        return result

#concate each row
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        width = len(matrix[0])
        length = len(matrix)
        left = 0
        right = width*length - 1
        while left <= right:
            mid = left + (right-left)//2
            row = mid//width
            col = mid%width
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid-1
            else:
                left = mid+1
        return False