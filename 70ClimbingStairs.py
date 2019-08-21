#top-down memo
class Solution:
    def climbStairs(self, n: int) -> int:
        table = {}
        return self.helper(table, n)
    def helper(self, table, n):
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1
        if n in table:
            return table[n]
        table[n]= self.helper(table, n-1) + self.helper(table, n-2)
        return table[n]
#DP
class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0 for i in range(n+1)]
        table[0] = 1
        table[1] = 1
        for i in range(2, n+1):
            table[i] = table[i-1] + table[i-2]
        
        return table[n]