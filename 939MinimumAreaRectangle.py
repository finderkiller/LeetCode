#Facebook interview, find one rectangle combination, return combination
#sol1: brute force, time: O(N^4), space: O(N)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        collection = []
        #points.sort(key=lambda x:(x[0], x[1]))
        self.col_table = {}
        self.row_table = {}
        self.min_area = sys.maxsize
        for row, col in points:
            if row not in self.row_table:
                self.row_table[row] = []
            self.row_table[row].append((row, col))
            if col not in self.col_table:
                self.col_table[col] = []
            self.col_table[col].append((row, col))
        for row, col in points:
            collection.append((row, col))
            if self.helper(row, col, collection, "col"):
                return collection
            collection.pop()
        return []
    def helper(self, row, col, collection, flag):
        if len(collection) == 4 and collection[-1][0] == collection[0][0]:
            return True
        elif len(collection) == 4:
            return False
        if flag == "col":
            for next_row, next_col in self.col_table.get(col):
                if next_row == row:
                    continue
                collection.append((next_row, next_col))
                if self.helper(next_row, next_col, collection, "row"):
                    return True
                collection.pop()
        else:
            for next_row, next_col in self.row_table.get(row):
                if next_col == col:
                    continue
                collection.append((next_row, next_col))
                if self.helper(next_row, next_col, collection, "col"):
                    return True
                collection.pop()
#Facebook interview, find one rectangle combination, return combination
#sol2: using diagnol, time: O(N^2), space: O(N)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        for x, y in points:
            points_set.add((x, y))
        for idx in range(len(points)-1):
            for idj in range(idx, len(points)):
                x0 = points[idx][0]
                y0 = points[idx][1]
                x1 = points[idj][0]
                y1 = points[idj][1]
                if x0 == x1 or y0 == y1:
                    continue
                if (x1, y0) not in points_set or (x0, y1) not in points_set:
                    continue
                return [(x0, y0), (x1, y1), (x1, y0), (x0, y1)]
        return []

#sol1: brute force, time: O(N^4), space:O(N) 
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        collection = []
        points.sort(key=lambda x:(x[0], x[1]))
        self.col_table = {}
        self.row_table = {}
        self.min_area = sys.maxsize
        for row, col in points:
            if row not in self.row_table:
                self.row_table[row] = []
            self.row_table[row].append((row, col))
            if col not in self.col_table:
                self.col_table[col] = []
            self.col_table[col].append((row, col))
        for row, col in points:
            collection.append((row, col))
            self.helper(row, col, collection, "col")
            collection.pop()
        return self.min_area if self.min_area != sys.maxsize else 0
    def helper(self, row, col, collection, flag):
        if len(collection) == 4 and collection[-1][0] == collection[0][0]:
            self.min_area = min(self.min_area, self.getArea(collection))
            return
        elif len(collection) == 4:
            return
        if flag == "col":
            for next_row, next_col in self.col_table.get(col):
                if next_row == row:
                    continue
                collection.append((next_row, next_col))
                self.helper(next_row, next_col, collection, "row")
                collection.pop()
        else:
            for next_row, next_col in self.row_table.get(row):
                if next_col == col:
                    continue
                collection.append((next_row, next_col))
                self.helper(next_row, next_col, collection, "col")
                collection.pop()
    def getArea(self, result):
        diff1 = abs(result[0][0]-result[1][0]) + abs(result[0][1]-result[1][1])
        diff2 = abs(result[1][0]-result[2][0]) + abs(result[1][1]-result[2][1])
        return diff1*diff2

#sol2: using diagonal + hash_set, time: O(N^2), space: O(N)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        min_area = sys.maxsize
        for x, y in points:
            points_set.add((x, y))
        for idx in range(len(points)-1):
            for idj in range(idx, len(points)):
                x0 = points[idx][0]
                y0 = points[idx][1]
                x1 = points[idj][0]
                y1 = points[idj][1]
                if x0 == x1 or y0 == y1:
                    continue
                if (x1, y0) not in points_set or (x0, y1) not in points_set:
                    continue
                min_area = min(min_area, abs(x0-x1)*abs(y0-y1))
        return min_area if min_area != sys.maxsize else 0