class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for i in range(n)] for j in range(n)]
        rowup = 0
        rowdown = len(result) - 1
        colleft = 0 
        colright = len(result[0]) - 1
        value = 0
        while rowup <= rowdown:
            for col in range(colleft, colright+1):
                value += 1
                result[rowup][col] = value
            for row in range(rowup+1, rowdown+1):
                value += 1
                result[row][colright] = value
            if rowup < rowdown:
                for col in range(colright-1, colleft, -1):
                    value += 1
                    result[rowdown][col] = value
            if colleft < colright:
                for row in range(rowdown, rowup, -1):
                    value += 1
                    result[row][colleft] = value
            rowup +=1
            rowdown -=1
            colleft +=1
            colright -=1
        return result