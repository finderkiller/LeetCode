#google interview1, 
# 第一问就是一个手机屏幕，上下滑动，所以宽度是一样的，每一行letter不一样。get the number of the same row
#brute force: time: O(n^3), space: O(1)
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        width = len(img1[0])
        height = len(img1)
        result = 0
        for row_offset in range(height):
            result = max(result, self.helper(img1, img2, row_offset))
        return result
    def helper(self, A, B, row_offset):
        over_lap_down = 0
        over_lap_up = 0
        col_same = True
        #down
        for row in range(row_offset, len(A)):
            for col in range(len(A[0])):
                if A[row][col] != B[row-row_offset][col]:
                    col_same = False
                    break
            if col_same:
                over_lap_down += 1
        #up
        col_same = True
        for row in range(0, len(A)-row_offset):
            for col in range(len(A[0])):
                if A[row][col] != B[row+row_offset][col]:
                    col_same = False
                    break
            if col_same:
                over_lap_up += 1
        return max(over_lap_down, over_lap_up)

#column hash: time: O(n^2), space: O(1)
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        width = len(img1[0])
        height = len(img1)
        self.A_tuple_hash = {}
        self.B_row_hash = {}
        result = 0
        for row in range(height):
            self.A_tuple_hash[row] = tuple(img1[row][col] for col in range(width))
            self.B_row_hash[row] = set()
            self.B_row_hash[row].add(tuple(img2[row]))
            
        for row_offset in range(height):
            result = max(result, self.helper(img1, img2, row_offset))
        return result
    def helper(self, A, B, row_offset):
        over_lap_down = 0
        over_lap_up = 0
        #down
        for row in range(row_offset, len(A)):
            if self.A_tuple_hash[row] in self.B_row_hash[row-row_offset]:
                over_lap_down += 1
        #up
        for row in range(0, len(A)-row_offset):
            if self.A_tuple_hash[row] in self.B_row_hash[row+row_offset]:
                over_lap_up += 1
        return max(over_lap_down, over_lap_up)

#第二问是一般的大小一样的两个屏幕，但是可以平行和上下滑动，求overlap number of pixel
#brute force: time: O(n^4), space: O(1)
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        width = len(img1[0])
        height = len(img1)
        result = 0
        for row_offset in range(height):
            for col_offset in range(width):
                result = max(result, self.helper(img1, img2, row_offset, col_offset))
        return result
    def helper(self, A, B, row_offset, col_offset):
        over_lap_down_right = 0
        over_lap_down_left = 0
        over_lap_up_right = 0
        over_lap_up_left = 0
        #down-right
        for row in range(row_offset, len(A)):
            for col in range(col_offset, len(A[0])):
                if A[row][col] == B[row-row_offset][col-col_offset]:
                    over_lap_down_right += 1
        #down-left
        for row in range(row_offset, len(A)):
            for col in range(0, len(A[0])-col_offset):
                if A[row][col] == B[row-row_offset][col+col_offset]:
                    over_lap_down_left += 1
        #up-right
        for row in range(0, len(A)-row_offset):
            for col in range(col_offset, len(A[0])):
                if A[row][col] == B[row+row_offset][col-col_offset]:
                    over_lap_up_right += 1
        #up_left
        for row in range(0, len(A)-row_offset):
            for col in range(0, len(A[0])-col_offset):
                if A[row][col] == B[row+row_offset][col+col_offset]:
                    over_lap_up_left += 1
        return max(over_lap_down_right, over_lap_down_left, \
                   over_lap_up_right, over_lap_up_left)

#LC 835
#sol1: brute force, time: O(n^4), space: O(1)
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        width = len(img1[0])
        height = len(img1)
        result = 0
        for row_offset in range(height):
            for col_offset in range(width):
                result = max(result, self.helper(img1, img2, row_offset, col_offset))
        return result
    def helper(self, A, B, row_offset, col_offset):
        over_lap_down_right = 0
        over_lap_down_left = 0
        over_lap_up_right = 0
        over_lap_up_left = 0
        #down-right
        for row in range(row_offset, len(A)):
            for col in range(col_offset, len(A[0])):
                if A[row][col] == 1 and B[row-row_offset][col-col_offset] == 1:
                    over_lap_down_right += 1
        #down-left
        for row in range(row_offset, len(A)):
            for col in range(0, len(A[0])-col_offset):
                if A[row][col] == 1 and B[row-row_offset][col+col_offset] == 1:
                    over_lap_down_left += 1
        #up-right
        for row in range(0, len(A)-row_offset):
            for col in range(col_offset, len(A[0])):
                if A[row][col] == 1 and B[row+row_offset][col-col_offset] == 1:
                    over_lap_up_right += 1
        #up_left
        for row in range(0, len(A)-row_offset):
            for col in range(0, len(A[0])-col_offset):
                if A[row][col] == 1 and B[row+row_offset][col+col_offset] == 1:
                    over_lap_up_left += 1
        return max(over_lap_down_right, over_lap_down_left, \
                   over_lap_up_right, over_lap_up_left)

#sol2: hash_table, key is (diff_row, diff_col), time: O(n^2), space: O(n)
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        point1 = []
        point2 = []
        table = {}
        area = 0
        for row in range(len(img1)):
            for col in range(len(img1[0])):
                if img1[row][col] == 1:
                    point1.append((row, col))
                if img2[row][col] == 1:
                    point2.append((row, col))
        for img1_row, img1_col in point1:
            for img2_row, img2_col in point2:
                if (img1_row-img2_row, img1_col-img2_col) not in table:
                    table[(img1_row-img2_row, img1_col-img2_col)] = 0
                table[(img1_row-img2_row, img1_col-img2_col)] += 1
                area = max(area, table[(img1_row-img2_row, img1_col-img2_col)])
        return area