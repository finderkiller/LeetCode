class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle == None:
            return 0
        table = {}
        return self.helper(triangle, table, 0, 0)
    def helper(self, triangle, table, idx, level):
        if len(triangle) == 0:
            return 0
        if (level, idx) in table:
            return table[(level, idx)]
        table[(level, idx)] = triangle[0][idx] + min(self.helper(triangle[1:], table, idx, level+1), self.helper(triangle[1:], table, idx+1, level+1))
        return table[(level, idx)]


#DP
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle == None:
            return 0
        table = []
        for level in range(len(triangle)):
            table.append([])
            for idx in range(level+1):
                table[level].append(0)

        table.append([0 for i in range(len(triangle[-1]) + 1)])
        for level in range(len(table)-2, -1, -1):
            for idx in range(level+1):
                table[level][idx] = triangle[level][idx] + min(table[level+1][idx], table[level+1][idx+1])
        return table[0][0]
                    
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle == None:
            return 0
        table = [0 for i in range(len(triangle)+1)]
        for level in range(len(triangle)-1, -1, -1):
            for idx in range(level+1):
                table[idx] = min(table[idx], table[idx+1]) + triangle[level][idx]
        return table[0]
            