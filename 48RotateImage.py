class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        rowup = 0 
        rowdown = len(matrix)-1
        colleft = 0
        colright = len(matrix)-1
        while rowup < rowdown:
            for col in range(colleft, colright):
                offset = col - colleft
                tmp = matrix[rowup][col]
                matrix[rowup][col] = matrix[rowdown-offset][colleft]
                matrix[rowdown-offset][colleft] = matrix[rowdown][colright-offset]
                matrix[rowdown][colright-offset] = matrix[rowup+offset][colright]
                matrix[rowup+offset][colright] = tmp
            rowup+=1
            rowdown-=1
            colleft+=1
            colright-=1