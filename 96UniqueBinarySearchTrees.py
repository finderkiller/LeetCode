# recursive
class Solution:
    def numTrees(self, n: int) -> int:
        return self.helper(n)
    def helper(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        result = 0
        for idx in range(n):
            result += self.helper(idx)*self.helper(n-idx-1)
        return result

# recursive, memo
class Solution:
    def numTrees(self, n: int) -> int:
        self.table = {}
        return self.helper(n)
    def helper(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n in self.table:
            return self.table[n]
        result = 0
        for idx in range(n):
            result += self.helper(idx)*self.helper(n-idx-1)
        self.table[n] = result
        return result

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