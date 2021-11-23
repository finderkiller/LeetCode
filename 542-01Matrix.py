#brute force
#O((m*n)^2)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        table = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]
        for row in range(len(table)):
            for col in range(len(table[0])):
                if mat[row][col] == 0:
                    table[row][col] = 0
                    continue
                table[row][col] = self.BFS(mat, row, col)
        return table
                
    def BFS(self, mat, start_row, start_col):
        visited = set()
        step = 0
        queue = []
        queue.append((start_row, start_col))
        visited.add((start_row, start_col))
        step = 0
        while len(queue) > 0:
            next_queue = []
            for row, col in queue:
                if row-1 >= 0 and (row-1, col) not in visited:
                    if mat[row-1][col] == 1:
                        visited.add((row-1, col))
                        next_queue.append((row-1, col))
                    else:
                        return step+1
                if row+1 < len(mat) and (row+1, col) not in visited:
                    if mat[row+1][col] == 1:
                        visited.add((row+1, col))
                        next_queue.append((row+1, col))
                    else:
                        return step+1
                if col-1 >= 0 and (row, col-1) not in visited:
                    if mat[row][col-1] == 1:
                        visited.add((row, col-1))
                        next_queue.append((row, col-1))
                    else:
                        return step+1
                if col+1 < len(mat[0]) and (row, col+1) not in visited:
                    if mat[row][col+1] == 1:
                        visited.add((row, col+1))
                        next_queue.append((row, col+1))
                    else:
                        return step+1
            step += 1
            queue = next_queue
        return step+1


#BFS, ensure that all 0 have been visited
#time: O(m*n)
#space: O(m*n)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        table = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]
        queue = []
        visited = set()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))
        step = 0
        while len(queue) > 0:
            next_queue = []
            for row, col in queue:
                for next_row, next_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if next_row < 0 or next_row == len(mat) or next_col < 0 or next_col == len(mat[0]):
                        continue
                    if (next_row, next_col) in visited:
                        continue
                    if mat[next_row][next_col] == 1:
                        table[next_row][next_col] = step+1
                        next_queue.append((next_row, next_col))
                        visited.add((next_row, next_col))
            queue = next_queue
            step += 1
        return table
                

#google question, find boundry
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        boundry = set()
        queue = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    
        for row, col in queue:
            if row-1 >= 0 and mat[row-1][col] == 1:
                boundry.add((row-1, col))
            if row+1 < len(mat) and mat[row+1][col] == 1:
                boundry.add((row+1, col))
            if col-1 >= 0 and mat[row][col-1] == 1:
                boundry.add((row, col-1))
            if col+1 < len(mat[0]) and mat[row][col+1]:
                boundry.add((row, col+1))
        return list(boundry)  
                
        
        