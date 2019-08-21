class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        return self.helper(matrix, 0, len(matrix[0])-1, target)
    def helper(self, matrix, row, col, target):
        if row >= len(matrix) or col < 0:
            return False
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            return self.helper(matrix, row, col-1, target)
        else:
            return self.helper(matrix, row+1, col, target)
# Binary search
class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def isInbound(self, matrix):
        return self.row >= 0 and self.row < len(matrix) and self.col >=0 and self.col <len(matrix[0])
    def isBefore(self, coordinate):
        return self.row <= coordinate.row and self.col <= coordinate.col
    
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        return self.helper(matrix, Coordinate(0, 0), Coordinate(len(matrix)-1, len(matrix[0])-1), target)
        
    def helper(self, matrix, start, end, target):
        if not start.isInbound(matrix) or not end.isInbound(matrix):
            return False
        if not start.isBefore(end):
            return False
        dist = min(end.row-start.row, end.col-start.col)
        pstart = Coordinate(start.row, start.col)
        pend = Coordinate(start.row+dist, start.col+dist)
        mid = Coordinate(0, 0)
        
        while pstart.isBefore(pend):
            mid.row = pstart.row + (pend.row-pstart.row)//2
            mid.col = pstart.col + (pend.col-pstart.col)//2
            
            if matrix[mid.row][mid.col] == target:
                return True
            elif matrix[mid.row][mid.col] > target:
                pend.row = mid.row-1
                pend.col = mid.col-1
            else:
                pstart.row = mid.row+1
                pstart.col = mid.col+1
        return self.partition(matrix, start, end, pstart, target)
    def partition(self, matrix, start, end, pstart, target):
        rightupstart = Coordinate(start.row, pstart.col)
        rightupend = Coordinate(pstart.row-1, end.col)
        leftdownstart = Coordinate(pstart.row, start.col)
        leftdownend = Coordinate(end.row, pstart.col-1)
        
        return self.helper(matrix, rightupstart, rightupend, target) or self.helper(matrix, leftdownstart, leftdownend, target)
        