class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        rowup = 0
        rowdown = len(matrix)-1
        colleft = 0
        colright = len(matrix[0])-1
        
        while(rowup <= rowdown and colleft <= colright):
            for col in range(colleft, colright+1):
                result.append(matrix[rowup][col])
            for row in range(rowup+1, rowdown+1):
                result.append(matrix[row][colright])
            if rowup < rowdown:
                for col in range(colright-1, colleft, -1):
                    result.append(matrix[rowdown][col])
            if colleft < colright:
                for row in range(rowdown, rowup, -1):
                    result.append(matrix[row][colleft])
            rowup += 1
            rowdown -= 1
            colleft +=1
            colright -=1
        return result