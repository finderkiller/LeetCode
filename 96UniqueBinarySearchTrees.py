# memo
class Solution:
    def numTrees(self, n: int) -> int:
        table = {}
        return self.helper(1, n, table)
    
    def helper(self, start, end, table):
        if start > end:
            return 1
        if (start, end) in table:
            return table[(start, end)]
        result = 0
        for value in range(start, end+1):
            left = self.helper(start, value-1, table)
            right = self.helper(value+1, end, table)
            result += left * right
        table[(start, end)] = result
        return result

# memo, 不用start end
class Solution:
    def numTrees(self, n: int) -> int:
        table = [0 for i in range(n+1)]
        return self.helper(n, table)
    def helper(self, n, table):
        if n==0:
            return 1
        if n == 1:
            return 1
        if table[n] != 0:
            return table[n]
        for left_nums in range(n):
            table[n] += self.helper(left_nums, table) * self.helper(n-1-left_nums, table)
        return table[n]

# bottom-up
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        table = [0 for i in range(n+1)]
        table[0] = 1
        table[1] = 1
        for idx in range(2, len(table)):
            for left_num in range(idx):
                table[idx] += table[left_num] * table[idx-left_num-1]
        return table[n]