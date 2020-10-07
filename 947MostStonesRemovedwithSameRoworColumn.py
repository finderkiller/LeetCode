class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        if not stones:
            return 0
        input = map(tuple, stones)
        self.visited = set()
        self.dict_row = {}
        self.dict_col = {}
        for row, col in input:
            if row not in self.dict_row:
                self.dict_row[row] = [col]
            else:
                self.dict_row[row].append(col)
            if col not in self.dict_col:
                self.dict_col[col] = [row]
            else:
                self.dict_col[col].append(row)
        
        self.result = 0
        for row, col in input:
            if (row, col) in self.visited:
                continue
            self.helper(row, col)
        return self.result
    
    def helper(self, input_row, input_col):
        self.visited.add((input_row, input_col))
        for col in self.dict_row[input_row]:
            if (input_row, col) in self.visited:
                continue
            self.result += 1
            self.helper(input_row, col)
        for row in self.dict_col[input_col]:
            if (row, input_col) in self.visited:
                continue
            self.result += 1
            self.helper(row, input_col)